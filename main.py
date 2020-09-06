from FunCryptography.lib.interface import *
from FunCryptography.lib.file import *



while True:
    # Create a menu title between two dashed line and
    headLine("MAIN MENU")
    # create an enumerated menu.
    mainMenu = ["Write a Text", "Encode File", "Decoding", "Exit"]
    showMenu = option(mainMenu)

    # The purpose of Write a Text Option is for users write their text direct on screen and then save it or not.
    if showMenu == 1:
        # write a text on the screen
        text = str(input('Type your text here: '))
        while True:
            headLine('What do you wanto to do with the text typed?')
            # Menu to decide what to do with the text typed on the screen
            writeMenu = ["Save the file", "Encode and Save the file", "Exit without saving"]
            showMenuW = option(writeMenu)
            if showMenuW == 1:
            # Set the file name and verifies whether it exist or not.
                fileName = input("Type the file name: ")
                if not fileExist(fileName):
                    # If the file name does not exist it'll create a new file and put the text into.
                    writeFile(fileName, text)
                    headLine("File saved")
                    break
                else:
                    headLine('This file already exist.')
            if showMenuW == 2:
                # Type a file name for analyses process.
                fileName = input("Type the file name: ")
                # Analyse whether file name typed exists and register the encoded text in file.
                if not fileExist(fileName):
                    encText = encoding(text)
                    writeFile(fileName, encText)
                    print(f"{fileName} saved.")
                    break
                else:
                    print(f'{fileName} Already exist. Try other name.')
            if showMenuW == 3:
                print("Exiting without save")
                break
    # Encode File menu option is for users that have a file to be encoded.
    if showMenu == 2:
        while True:
            # Type a file name for analyse process.
            fileName = input("Type your file name: ")
            # verify if exist a file with the name typed by user and show up text encoded on screen.
            if fileExist(fileName):
                showBeforeSave = getTextEncoded(fileName)
                print(showBeforeSave)
                print(dashedLine())

                headLine("Encode File Menu")
                # The menu for users decide whether save encoded text in a new file or not.
                encodeMenu = ["Save the Encoded File", "Exit without saving"]
                showMenuE = option(encodeMenu)
                if showMenuE == 1:
                    # reads the file and return the text in a string
                    a = getTextEncoded(fileName)
                    # Asks a name for the new file where the encoded text version will be registered.
                    newFile = input("Type a name for encoded file: ")
                    writeFile(newFile, a)
                    headLine(f"{newFile}File saved.")
                    break
                if showMenuE == 2:
                    print("File not saved. Exiting the software")
                    break
            else:
                print(f"The file {fileName} was not found.")
    if showMenu == 3:
        while True:
            # Get a name to be analysed.
            fileName = input("Type the file name: ")
            # This function verifies if exist a file with the name typed and show up decoded text on screen.
            if fileExist(fileName):
                showBeforeSave = getTextDecoded(fileName)
                print(showBeforeSave)
                headLine("Decoding Menu")
                # This is a menu for user decide whether to save decoded text in a new file or not.
                deCodeMenu = ["Save the Decoded File", "Exit without saving"]
                showMenuD = option(deCodeMenu)
                if showMenuD == 1:
                    # This function decode file text.
                    a = getTextDecoded(fileName)
                    # this function give a name for the new file and write the decoded text in it.
                    newFile = input("Type a name for decoded file: ")
                    writeFile(newFile, a)
                    print(f'{fileName} decoded file saved.')
                    break
                if showMenuD == 2:
                    print("Exiting Without saving.")
                    break
    if showMenu == 4:
        headLine("Exiting the software")
        break