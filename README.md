# TTF_Injector
Script that adds svg symbols to the .ttf file

Easy way to simply add .svg files to .ttf files. Meaning you can replace a letter with a symbol. 
Perfect if you wanna display symbols instead of text, or just simply use an empty codepoint.
Files inside svg folder and values inside mapping.json is example, test if you want ;D

<img width="1331" height="211" alt="image" src="https://github.com/user-attachments/assets/4471df8b-615c-4660-8d28-be1f54c5a595" />


How to use:
1. Download FontForge (this will be the program used in editing the .ttf file)
2. Add the file path .exe path to your enviroment variables so that the script can run the FontForge on its own.
This is usually in "C:\Program Files (x86)\FontForgeBuilds\bin".
3. Inside your TTF_Injector folder, put your .svg files inside the svg folder.
4. Open the mapping.json and define which .svg file sud be inserted into which codepoint.
Example:
  [
    "emote_sunglasses.svg", //SVG file
    "E000" //Codepoint
  ],
  [
    "emote_flame.svg", //SVG file
    "E001" //Codepoint
  ],

5.Now put your .ttf file you wanna change into the TTF_Injector folder.
6. run the "run windows" .bat file.

7. Enjoy letter conversion!


