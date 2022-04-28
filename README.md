******

* Required Python packages are  pandas, requests, streamlit
  - pip install requests
  - pip install pandas
  - pip install streamlit


This project is divided into 3 parts

 * A. Use twitter api to get basic information about NBA stars (12 of them) and who they follow.
The twitter data of these stars is used to study if any of the people they follow are also NBA stars, i.e. if there are stars who follow each other.
This data is saved as a csv file.

 * B. Based on the data obtained in part A, create a database, sqlite3 and create 2 tables to save the data.

 * C. Use streamlit to create a short web app.
   1. Let the user choose whether to display all the data of the players or not.
   2. Let the user select a particular player and query the detailed results.
   3. Show some statistics.



 * D. Data Structure, build a tree like this
```

                                Root
                      /          |             \
                    /            |              \
                  /              |               \
            "KDTrey5",      "JHarden13",        "russwest44",      ... "player_12"
         /      |      \
        /       |        \
      /         |         \
  following_1 following_2,  following_3,  ...  following_100

```



* Required Python packages are  pandas, requests, streamlit
pip install requests
pip install pandas
pip install streamlit



E. run this app
* Use command prompt (win), terminal (mac) to switch to the directory where the files is located:
  $ cd 'your file folder path'
Then
  $ streamlit run app.py

  # or just run Run_app.py
  $ streamlit run app.py

  # go to: http://localhost:8501
