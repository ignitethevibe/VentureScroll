# - Tutorial Level





class pLevel():
    # This is a generic super-class to define a level
    # Create a child class for each level with level specific info

    def __init__(self, player):
        # Constructor. Pass in a handle to player. Needed for when moving platforms
        # collide with the player

        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()

        # -- 7/27
        self.extra_list = pygame.sprite.Group()

        self.player = player


        # how far world has been scrolled
        self.world_shift = 0


    def update(self):
        self.platform_list.update()

    def draw(self, screen):

        # Draw Background
        screen.blit(hallway, (0,0))

        # Draw all sprite lists
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)



    def shift_world(self, shift_x):

        # keep track of shift amount
        self.world_shift += shift_x

        # go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

        for extra in self.extra_list:
            extra.rect.x += shift_x


class Level_00(pLevel):

    def __init__(self, player):


        # call parent constructor
        Level.__init__(self, player)

        self.level_limit = -1500

        # array of platform (w,h), (x,y)
        level = [,
                ]


        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)


        # -- Make Extra's as blocks with texts
        # -- to explain gameplay
