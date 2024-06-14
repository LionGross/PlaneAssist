# PlaneAssist
![Image not available](Images/PlaneAssist_Banner.png)
## Table of Contents
1. [Project Description](#project-description)
    - [Disclaimer](#disclaimer)
2. [Features](#features)
    - [Files for this project](#files-for-this-project)
3. [Installation](#installation)
4. [Usage](#usage)
    - [Command-Line Arguments](#command-line-arguments)
    - [Supported Languages](#supported-languages)
    - [Before you start](#before-you-start-some-things-to-be-aware-of)
    - [Trouble finding language codes](#trouble-finding-language-code)
    - [Start](#start)

5. [Methods of the class PlaneAssist](#methods-of-the-class-planeassist)
    - [wing_area_func](#wing_area_func)
    - [stall_speed_func](#stall_speed_func)
    - [thrust_func](#thrust_func)
    - [flight_time_func](#flight_time_func)
    - [range_func](#range_func)
    - [all_in_one_func](#all_in_one_func)
6. [Functions outside the PlaneAssist class](#functions-outside-the-planeassist-class)
    - [main()](#main)
    - [arg_checker()](#arg_checker)
    - [check_internet_connection()](#check_internet_connection)
    - [translate_n_print](#translate_n_print)
    - [manage_data()](#manage_data)
    - [get_float_input()](#get_float_input)
    - [save_data()](#save_data)
    - [terminate()](#terminate)

## Project Description:
PlaneAssist runs in your terminal and helps you calculate key parameters for aircraft design. 

### Disclaimer
This Python program is provided for educational
purposes only. It calculates the wing area, stall speed,
the thrust required, and other properties of an airplane
based on certain input parameters.

The calculations are based on simplified physics and do not
take into account all the complex variables and conditions
that can affect an airplane's performance in real-world scenarios.

The program is not intended to be used for actual flight planning
or aircraft design. The results should not be used for making
decisions that can result in harm to people or property.

The author of this program is not responsible for any damages
or losses arising from the use of this program.

For these calculations the ICAO standard atmosphere 1993 is used.

Additionally, this program includes a language translation feature.
The accuracy of translations is not guaranteed, and the program's author
is not responsible for errors or inaccuracies in the translated content.

Always consult with a certified aviation professional or use
certified software for flight planning and aircraft design.

USE AT YOUR OWN RISK.

## Features
- **Wing Area Calculator**: Calculates the minimum recommended wing area.
- **Stall Speed Calculator**: Calculates the stall speed of the aircraft.
- **Thrust Required Calculator**: Calculates the minimum thrust required for flight.
- **Flight Time Calculator**: Estimates the flight time for an electric aircraft.
- **Range Calculator**: Determines the range for an electric aircraft.
- **All-In-One Calculator**: Provides a comprehensive calculation of all the above parameters in one go.
- **Save Results**: Allows users to save their calculated results into an Excel file.
- **Language Translation**: Program supports multiple languages.

### Files for this project
- **project.py** - The implementation of this program.
- **test_project.py** - Tests to, well, test the program.
- **requirements.txt** - The required libraries, installable with pip, for this program.
- **README.md** - The code for the documentation you are reading now.
- **DONT_EDIT.xlsx** - A template which is needed to save your data to an .xlsx file (please do not edit).

## Installation

- Make sure you have Python 3.10 or higher installed.
- For the program to work, you must download at least these files and save them in the same folder:
   - project.py
   - requirements.txt
   - DONT_EDIT.xlsx
- Once you've downloaded these files, run this command from the directory where the program is
stored to install the necessary libraries:

```
pip install -r requirements.txt
```

## Usage
### Command Line Arguments:
All Arguments are optional.
- **Altitude** (```-a```/```--altitude```): Altitude in meters above mean sea level (default: 0).
- **Language** (```-l```/```--language```): IETF language tag for translations (default: en).

### Supported Languages
Language tags for some popular (but not all) supported languages:
  - Chinese (Traditional) -> ```zh-TW```
  - Chinese (Modern) -> ```zh-CN```
  - Hindi ->  ```hi```
  - Arabic -> ```ar```
  - Spanish -> ```es```
  - French -> ```fr```
  - German -> ```de```

### Before you start, some things to be aware of...

If you run the program in a language other than English
the program can run slower (depending on your Internet speed) due to the translation process.

As stated in the disclaimer, if you run the program in a language other than English, there may be translation errors, so be aware of that.

Besides the languages listed above, any language you can translate with Google Translate will work with this program,
if you have the correct language code (that's why I included both language codes for Chinese).

### Trouble finding language code
If you have trouble finding the right language code for your language,
you can go to ```https://translate.google.com/``` and select:

english -> your language

You should get a URL like this ```https://translate.google.com/?ucbcb=1&sl=auto&tl=ko&op=translate```
in you address bar (korean language in this example).
You find the language code after this part ```tl=```,
which is in this example ```ko``` for korean.

### Start
To Start the program, run this command in your terminal in the directory where you installed the code:
```
python project.py --altitude <altitude_in_meters> --language <language_code>
```
You are now in the main menu of the program, where you can choose from a list of calculators that you can run,
which looks like this:

- [[1] - Wing Area Calculator](#wing_area_func)
- [[2] - Stall Speed Calculator](#stall_speed_func)
- [[3] - Thrust Required Calculator](#thrust_func)
- [[4] - Flight Time Calculator](#flight_time_func)
- [[5] - Range Calculator](#range_func)
- [[6] - ´All In One´ Calculator](#all_in_one_func)
- [[T] - Terminate](#terminate)

Here you can simply type the number specific to the calculator.
The calculater will then start to ask questions about some parameters that you must know to perform these calculations.
After that the calculator will give you the result of the calculation.

## Methods of the class PlaneAssist
### menu()
Displays the PlaneAssist Main Menu and allows the user to select from various options for aircraft calculations.

### wing_area_func()
Calculate the wing area of the aircraft based on the maximum lift coefficient, mass of the aircraft,
and minimum flying velocity.

### stall_speed_func()
Calculate the stall speed of an aircraft in horizontal unaccelerated flight.

### thrust_func()
Calculate the thrust required for horizontal unaccelerated flight.

### flight_time_func()
Calculate the flight time of an electric aircraft for horizontal unaccelerated flight.

### range_func()
Calculate the range of an electric aircraft for horizontal unaccelerated flight.

### all_in_one_func()
Calculate wing area, stall speed, thrust required, flight time and range of an electric aircraft for
horizontal unaccelerated flight.

## Functions outside the PlaneAssist class
### main()
The main entry point of the PlaneAssist program.

Clears the terminal screen, checks for validity of
optional altitude input, initializes the PlaneAssist class,
checks the internet connection, and displays the welcome message
and disclaimer. Displays also a progress bar simulation before
displaying the main menu of the program to encourage reading of
the disclaimer.

### arg_checker()
This function parses the command-line arguments to retrieve the altitude and language information.

### check_internet_connection()
Check for an existing internet connection by trying to send a request to google.

### translate_n_print()
Translates text and prints it on the terminal window.

Translates the input text to a specified language if an internet
connection is available and the specified language is not English,
and then prints the translated text. If there is no internet
connection the text will be printed as it is (default english).
If a color is specified, the text is printed in the specified color.

### manage_data()
Manages the requests for the [get_float_input()](#get_float_input) function, stores and organizes the values gathered
and return a dictionary of input data.


### get_float_input()
Prompts the user to input a float value and handles wrong input.

### save_data()
Saves the provided data to an Excel file.

### terminate()
Prompt the user to confirm if they want to exit the program.
    If confirmed, terminate the program.

