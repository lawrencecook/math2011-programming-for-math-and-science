poem = "What is pink? a rose is pink By a fountain's brink. What is red? a poppy's red In its barley bed. What is blue? the sky is blue Where the clouds float thro'. What is white? a swan is white Sailing in the light. What is yellow? pears are yellow, Rich and ripe and mellow. What is green? the grass is green, With small flowers between. What is violet? clouds are violet In the summer twilight. What is orange? Why, an orange, Just an orange!"

color_codes = {"red":"\033[0;31m" , "pink": "\033[95m" , "blue": "\033[34m" , "white": "\033[37m" , "yellow": "\033[33m" , "green": "\033[32m" , "violet": "\033[35m" , "orange": "\033[33m"}

for color in color_codes:
    poem = poem.replace(color, color_codes[color] + color + "\033[0m")

print(poem)


