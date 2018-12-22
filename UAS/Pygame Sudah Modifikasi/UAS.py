import pygame
import random
import math
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PURPLE = (255, 0, 255)

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 650

Gambar = pygame.image.load('Background.png')
Background = pygame.transform.smoothscale(Gambar,(SCREEN_WIDTH,SCREEN_HEIGHT))

# --- Classes

class Wall(pygame.sprite.Sprite):
    """This class represents the bar at the bottom that the player controls """
 
    def __init__(self, x, y, width, height):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Block(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        self.meteor = pygame.image.load('Meteor.png')
        self.image = pygame.transform.scale(self.meteor, (30, 30))
        #self.image = pygame.Surface([20, 15])
        #self.image.fill(color)
 
        self.rect = self.image.get_rect()
    def reset_pos(self):
        """ Called when the block is 'collected' or falls off
            the screen. """
        self.rect.y = random.randrange(-700, -20)
        self.rect.x = random.randrange(10, SCREEN_WIDTH - 40)
 
    def update(self):
        """ Automatically called when we need to move the block. """
        self.rect.y += 1
 
        if self.rect.y > SCREEN_HEIGHT + self.rect.height :
            self.reset_pos()

class bigBlock(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        self.meteor = pygame.image.load('Meteor.png')
        self.image = pygame.transform.scale(self.meteor, (65, 65))
 
        self.rect = self.image.get_rect()
    def reset_pos(self):
        """ Called when the block is 'collected' or falls off
            the screen. """
        self.rect.y = random.randrange(-700, -20)
        self.rect.x = random.randrange(10, SCREEN_WIDTH - 80)

    def update(self):
        """ Automatically called when we need to move the block. """
        self.rect.y += 2
 
        if self.rect.y > SCREEN_HEIGHT + self.rect.height :
            self.reset_pos()

class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """
 
    def __init__(self, WIDTH, HEIGHT):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.width = WIDTH
        self.height = HEIGHT
        
        self.rocket = pygame.image.load('Pesawat.png')
        self.image = pygame.transform.scale(self.rocket, (self.width, self.height))
        #self.image = pygame.Surface([self.width, self.height])
        #self.image.fill(RED)
        self.rect = self.image.get_rect()

        self.rect.x = SCREEN_WIDTH / 2 - self.width / 2
        self.rect.y = SCREEN_HEIGHT - self.height

        self.change_x = 0
        self.change_y = 0
        self.walls = None

    def changespeed(self,x,y):
        self.change_x += x
        self.change_y += y

    def update(self):
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet. """
 
    def __init__(self, start_x, start_y, dest_x, dest_y):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Set up the image for the bullet
        self.image = pygame.Surface([4, 10])
        self.image.fill(PURPLE)
 
        self.rect = self.image.get_rect()
 
        # Move the bullet to our starting location
        self.rect.x = start_x
        self.rect.y = start_y

        self.floating_point_x = start_x
        self.floating_point_y = start_y
 
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff);
 
        velocity = 5
        self.change_x = math.cos(angle) * velocity
        self.change_y = math.sin(angle) * velocity
 
    def update(self):
        """ Move the bullet. """
 
        # The floating point x and y hold our more accurate location.
        self.floating_point_y += self.change_y
        self.floating_point_x += self.change_x
 
        # The rect.x and rect.y are converted to integers.
        self.rect.y = int(self.floating_point_y)
        self.rect.x = int(self.floating_point_x)
 
        # If the bullet flies of the screen, get rid of it.
        if self.rect.x < 0 or self.rect.x > SCREEN_WIDTH or self.rect.y < 0 or self.rect.y > SCREEN_HEIGHT:
            self.kill()
 
 
 
# --- membuat window
 
# inisialisasi Pygame
pygame.init()
 
#mengatur panjang lebar nya screen 
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 
# --- Sprite lists
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
# List of each block in the game
block_list = pygame.sprite.Group()

# List of each bigBlock in the game
bigblock_list = pygame.sprite.Group()

# List of each bullet
bullet_list = pygame.sprite.Group()

# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()


# --- membuat the sprites

for i in range(10):
    # This represents a block
    block = Block()
    bigblock = bigBlock()

    # Add the block to the list of objects
    block_list.add(block)
    bigblock_list.add(bigblock)
    all_sprites_list.add(block,bigblock)

    # mengatur lokasi block secara acak
    block.reset_pos()
    bigblock.reset_pos()

# --- make the tembok
wall = Wall(0, 0, 10, SCREEN_HEIGHT)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(SCREEN_WIDTH - 10, 0, 10, SCREEN_HEIGHT)
wall_list.add(wall)
all_sprites_list.add(wall)

# Create a red player block
player = Player(35, 80)
player.walls = wall_list
all_sprites_list.add(player)

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# This is a font we use to draw text on the screen (size 36)
font = pygame.font.Font(None, 36)

# Current score
score = 0

# Current level
level = 1



# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Fire a bullet if the user clicks the mouse button
        # Get the mouse position
        pos = pygame.mouse.get_pos()
        mouse_x = pos[0]
        mouse_y = pos[1]
        bullet = Bullet(player.rect.x + player.width / 2, player.rect.y, mouse_x, mouse_y)
##        pygame.mixer.music.load('Carefree.mp3')
##        pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
##        pygame.mixer.music.play()

        
        if event.type == pygame.MOUSEBUTTONDOWN:
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
            pygame.mixer.music.load('match1.wav')
            pygame.mixer.music.play()
            
        elif event.type == pygame.MOUSEBUTTONUP and level >= 6:
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
 
    all_sprites_list.update()

##    for bigblock in bigblock_list:
##        block_hit_list = pygame.sprite.spritecollide(bigblock, block_list, False)
##
##        for block in block_hit_list:
##            block.reset_pos()
 
    for bullet in bullet_list:
        # See if it hit a block
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
        
        # For each block hit, remove the bullet and add to the score
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            print(score)
            #pygame.mixer.music.load('Ghost.mp3')
            #pygame.mixer.music.play()
            
        if bullet.rect.y < -5:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    for bullet in bullet_list:
        bigblock_hit_list = pygame.sprite.spritecollide(bullet, bigblock_list, True)
       
        for bigblock in bigblock_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score+= 2
            print(score)
 
        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -5:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    for bullet in bullet_list:
        # See if it hit a block
        wall_hit_list = pygame.sprite.spritecollide(bullet, wall_list, False)

        # For each block hit, remove the bullet and add to the score
        for block in wall_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
 
        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    # Check to see if all the blocks are gone.
    # If they are, level up.
    if len(block_list) == 0 and len(bigblock_list) == 0:
        # Add one to the level
        level += 1
 
        # Add more blocks. How many depends on the level.
        # Also, an 'if' statement could be used to change what
        # happens customized to levels 2, 3, 4, etc.
        for i in range(level * 10):
            # This represents a block
            block = Block()
            bigblock = bigBlock()
 
            # Add the block to the list of objects
            block_list.add(block)
            bigblock_list.add(bigblock)
            all_sprites_list.add(block,bigblock)

            block.reset_pos()
            bigblock.reset_pos()
    
    # Clear the screen
    #screen.fill(WHITE)
    screen.blit(Background, (0,0))

    # Draw all the spites
    all_sprites_list.draw(screen)

    text = font.render("Score: "+str(score), True, RED)
    screen.blit(text, [10, 10])

    text = font.render("Level: "+str(level), True, RED)
    screen.blit(text, [10, 40])
    
    pygame.display.flip()
    
    clock.tick(70)

pygame.quit()
