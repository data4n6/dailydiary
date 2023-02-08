Organization

main.py     - MainApp()
    /kv     - *.kv files
    /images - Image Storage
    /db     - Database Storage

Objective

An app that logs daily activities to keep metrics on personal development inside of a sqlite3 db.
Same day entries will happen at different times of the day
    Script needs to:
        create database if one does not exist
        update data for current date, multiple times
        pull data for day to show what has been entered
        enter in null values for fields not entered
        charts need to incorporate null values in a way that do not negate metrics/averages
Features:
    update itself
    not delete db with updates
    backup db
    delete db, start from scratch
    modify records in db
    delete records in db
    about page with current version
    Capable of adding custom fields/metrics

Data Inputs:
    Date: 
        Today's Date - No need for time
    Weight:
        Daily Log, Chart showing daily metric
    Blood Pressure:
        Sys
        Dia
        Heartbeat
    KetoMojo:
        Glucose
        Ketosis
    Meditation/Workout:
        Yes/No - if yes, enable following
        Breathing Exercise:
            Yes/No - if yes, enable following
            Round 1 - Log Time
            Round 2 - Log Time
            Round 3 - Log Time
        Push-ups:
            Yes/No - if yes, enable following
            Without Breath  - Count Amount, chart showing daily metric
            With Breath     - Count Amount, chart showing daily metric
            Total           - Sum Both Amounts, chart showing daily metric
        Scissor Kicks:
            Yes/No - if yes, enable following
            Total - Count Amount, chart showing daily metric
        Plank:
            Yes/No - if yes, enable following
            Time - Log Time, chart showing daily metric
        Sit-ups:
            Yes/No - if yes, enable following
            Total - Count Amount, chart showing daily metric

Tasks:
    Create Base App that updates self from github
    Create Form
    Create Database function
    Store Database information

