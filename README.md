Steps:
1. Maintain a dictionary of users where each user has a first and last name, phone #, and stocks they are interested in tracking.
2. Each morning at 9:00 est, send out a text message to each user about their stocks.
    - Track changes from average of last week, where last week is defined as 1-7 days ago if current_day == Monday-Friday, 2-8 days ago if Saturday, 3-9 day ago if current_day == Sunday
    - 1 suggested move:
        - Sell / Buy certain stocks based on price / book ratio and change.
3. Zip up these files to make them compatible with AWS lambda
4. Run the files on AWS lambda using a task scheduler (for testing, use 5-minute increments rather than 1 day)
5. Create an AWS S3 bucket to hold user information.