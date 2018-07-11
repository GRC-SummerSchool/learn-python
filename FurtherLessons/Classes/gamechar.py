from random import randint


class ActionError(ValueError):
    pass

class CharacterError(ValueError):
    pass

class GameCharacter:

    MAX_STR = 16
    MIN_STR = 8

    WEAPONS = {4:6, 6:5, 8:4, 10:2, 12:0}

    def __init__(self, name, player, team, strength = 12, weapon = 6):
        """
        A class representing an approximate D&D-style game character.
        On their turn, a character can protect a teammate or attack an enemy.
        :param name: Character name
        :param player: Character player
        :param team: The character's team
        :param strength: Character's strength. Min 8, max 16. Dexterity = 24 - strength
        :param weapon: Character's weapon. One of (4, 6, 8, 10, 12). Higher weapon -> lower armor
        """
        self.name = name
        self.player = player
        self.team = team
        self.alive = True
        self.HP = 20


        # Dexterity set based on strength
        self.strength = min([max([strength,self.MIN_STR]), self.MAX_STR])
        self.dexterity = self.MIN_STR + self.MAX_STR - strength

        self.weapon = weapon
        self.armor = self.WEAPONS[self.weapon]

        self._HP = 20 + self.modifier(self.strength)
        self.AC = 10 + self.modifier(self.dexterity) + self.armor

        self.protecting = None
        self.protected = None


    def attack(self,gamecharacter):
        if not self.alive: raise CharacterError("%s is dead."%self.name)
        if self.team == gamecharacter.team: raise ActionError("Cannot attack your own team")

        if gamecharacter.protected:
            # Switch the target of the attack
            print("%s is protected by %s!"%(gamecharacter.name,gamecharacter.protected.name))
            gamecharacter = gamecharacter.protected

        if not gamecharacter.alive: raise ActionError("Can't beat a dead horse")

        attack = self.roll20() + self.modifier(self.strength)

        if attack >= gamecharacter.AC:
            damage = self.roll(self.weapon) + self.modifier(self.strength)

            print("Attack successful! %s did %i damage to %s"%(self.name,damage,gamecharacter.name))

            gamecharacter.HP -= damage

        else:
            print("Attack Misses!")
            return False

    def protect(self,gamecharacter):
        if not self.alive: raise CharacterError("%s is dead."%self.name)

        if self.team != gamecharacter.team: raise ActionError("Your team needs it more!")

        if gamecharacter.protected:
            gamecharacter.protected.unprotect()

        self.protecting = gamecharacter
        gamecharacter.protected = self

        print("%s is protecting %s from harm."%(self.name, gamecharacter.name))
        return True

    def unprotect(self):
        if self.protecting:
            print("%s stops protecting %s."%(self.name,self.protecting.name))
            self.protecting.protected = None
            self.protecting = None

    def initiative(self):
        return self.roll20() + self.modifier(self.dexterity)

    def get_HP(self):
        return self._HP

    def set_HP(self,hp):
        self._HP = hp

        was_alive = self.alive
        self.alive = self._HP > 0

        if was_alive and not self.alive:
            print("%s has died"%self.name)
            self.unprotect()

        if not was_alive and self.alive:
            print("%s has revived!"%self.name)

    HP = property(get_HP,set_HP)

    @staticmethod
    def roll(dice):
        return randint(0,dice)+1

    @staticmethod
    def roll20():
        return randint(0,20)+1

    @staticmethod
    def modifier(attr):
        return int((attr-10)/2)


