[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/_IojtdoU)
# StackIt Hiring Assignment

### Welcome to StackIt's hiring assignment! 🚀

**If you didn't get here through github classroom, are you sure you're supposed to be here? 🤨**


We are glad to have you here, but before you read what you're going to beat your head over for the next few hours (maybe days?), let's get a few things straight:
- We really appreciate honesty. Don't copy anyone else's assignment, it'll only sabotage your chances :P
- You're free to use any stack, and library of your choice. Use whatever you can get your hands on, on the internet!
- We love out of the box solutions. We prefer to call it *Jugaad* 
- This might be just the first round, but carries the most importance of all. Give your best, and we hope you have a fun time solving this problem.

## ✨ **Problem Statement: Crafting a CSV Importer for Google Sheets** ✨

**Context**:
Data analysts around the world 🌍, handle massive amounts of data to derive meaningful insights for their organization 📊. Among the tools they use, Google Sheets 📈 stands out due to its ease of use, accessibility, and collaborative features. However, many analysts have identified a recurring pain point: the cumbersome process of importing CSV files into Google Sheets repeatedly.

A typical week of an analyst in an e-commerce company 🛒 involves receiving multiple CSV files 📁 containing sales, inventory, customer feedback, and more. The data from these files needs to be meticulously analyzed and presented in the company’s weekly meetings. However, instead of diving directly into analysis, most analysts need to spend an inordinate amount of time just importing and structuring these CSV files into Google Sheets ⏳. This repetitive, time-consuming task reduces the efficiency of these professionals and delays the extraction of crucial insights 😫.

**Today, you are going to make their lives better.**

**Problem Statement**:
Make a CSV Importer for Google Sheets that lets users drag and drop CSV files onto the Google Sheet. The moment they drop the CSV file, allow them to select which columns to import 🗂️.

You get brownie points 🍪 if you can make it even easier by allowing them to filter the data as well before importing it into Google Sheets 🔍.

**Other pointers**:
- Import to Sheet – After validation and mapping, devise a method to populate the data into a chosen Google Sheet, either appending to existing data or creating a new sheet 📥📋.
- Optimize for Large Files – Large datasets are common in analytics. Your solution should effectively handle large CSV files (~15MB CSV file) without causing performance issues or prolonged waiting times 📈📦.

## Submission ⏰
The timeline for this submission is: **9AM, 30th Sept, 2023 - 12PM, 2nd Oct, 2023**

Some things you might want to take care of:
- Make use of git and commit your steps!
- Use good coding practices.
- Write beautiful and readable code. Well-written code is nothing less than a work of art.
- Use semantic variable naming.
- Your code should be organized well in files and folders which is easy to figure out.
- If there is something happening in your code that is not very intuitive, add some comments.
- Add to this README at the bottom explaining your approach (brownie points 😋)

Make sure you finish the assignment a little earlier than this so you have time to make any final changes.

Once you're done, make sure you **record a video** showing your project working. The video should **NOT** be longer than 120 seconds. While you record the video, tell us about your biggest blocker, and how you overcame it! Don't be shy, talk us through, we'd love that.

We have a checklist at the bottom of this README file, which you should update as your progress with your assignment. It will help us evaluate your project.

- [X] My code's working just fine! 🥳
- [ ] I have recorded a video showing it working and embedded it in the README ▶️
- [X] I have tested all the normal working cases 😎
- [X] I have even solved some edge cases (brownie points) 💪
- [ ] I added my very planned-out approach to the problem at the end of this README 📜

## Got Questions❓
Feel free to check the discussions tab, you might get something of help there. Check out that tab before reaching out to us. Also, did you know, the internet is a great place to explore 😛

## Developer's Section

## SheetSync: CSV Import & Filter
SheetSync is a web application that allows users to upload a CSV file, select specific columns from it, and add the selected data to a Google Sheet. Users can also provide a Google Sheet link to append their data to an existing sheet. This project utilizes the Google Sheets API for seamless integration with Google Sheets.

### Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Video](#Video)


### Features

- Upload a CSV file.
- Select specific columns from the CSV file.
- Create a new Google Sheet and add the selected data.
- Append data to an existing Google Sheet using a provided link.
- Utilizes the Google Sheets API for seamless integration with Google Sheets.

### Prerequisites

- [Python](https://www.python.org/) Ensure that you have Python installed on your computer.
- [Google Cloud Platform](https://cloud.google.com/) project with the Google Sheets API enabled.
- OAuth 2.0 credentials (client ID and client secret) for your Google Cloud project.

### Installation

1. Clone the repository:

    Open your terminal or command prompt and navigate to the directory where you want to clone the project. 

    Then, run the following command to clone the repository:
    ```ruby
    git clone https://github.com/StackItHQ/stackit-hiring-assignment-KetanAgrawal2002.git
    ```

3. Navigate to the project directory:
   
    ```ruby
    cd stackit-hiring-assignment-KetanAgrawal2002
    ```

4. Install the required dependencies:

     Double click requirements.bat


6. Set up the Google Calendar credentials:
     
    Download and place the credentials.json file (which contains your Google Sheet API credentials) in the project root directory and also add the access token and refresh token in token.json

### Usage
5. Start the application:

     Once you have all the prerequisites ready, you can run the project locally by executing the index.py file using the command:  

    ```ruby
    streamlit run index.py
    ```


### Video





