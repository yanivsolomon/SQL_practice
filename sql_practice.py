import time
from selenium import webdriver
import pytest

# An SQL practice using Python and Selenium (can also be considered as a functional test for sqlbolt.com).
# File contains:
# SELECT statement practice.
# CREATE TABLE statement practice.
# UPDATE statement practice.
# DELETE statement practice.
# INSERT statement practice.
# JOIN statement practice.

# setup and teardown (fixture)
@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Edge(executable_path="C:\Program Files (x86)\msedgedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print("test completed")


# SELECT practice:
def test_select(test_setup):
    driver.get("https://sqlbolt.com/lesson/select_queries_introduction")
    time.sleep(3)
    # answer question #1
    clearbutton = driver.find_element_by_xpath("//a[@class='clear']")
    clearbutton.click()
    text_field = driver.find_element_by_xpath("//textarea[@class='ace_text-input']")
    text_field.send_keys("select title from movies")
    time.sleep(3)
    # answer question #2
    clearbutton.click()
    text_field.send_keys("select director from movies")
    time.sleep(3)
    # answer question #3
    clearbutton.click()
    text_field.send_keys("select title, director from movies")
    time.sleep(3)
    # answer question #4
    clearbutton.click()
    text_field.send_keys("select title, year from movies")
    time.sleep(3)
    # answer question #5
    clearbutton.click()
    text_field.send_keys("select * from movies")
    time.sleep(3)


# CREATE TABLE practice:
def test_create_table(test_setup):
    driver.get("https://sqlbolt.com/lesson/creating_tables")
    time.sleep(3)
    # answer question #1
    clearbutton = driver.find_element_by_xpath("//a[@class='clear']")
    clearbutton.click()
    text_field = driver.find_element_by_xpath("//textarea[@class='ace_text-input']")
    # create a table called "Database" with these values "Name"(TEXT), "Version"(FLOAT), "D_COUNT"(INT)
    text_field.send_keys("""CREATE TABLE Database (Name TEXT, Version FLOAT, Download_count INTEGER)""")
    run_query_btn = driver.find_element_by_xpath("//a[@class='submit']")
    run_query_btn.click()
    time.sleep(3)

# UPDATE TABLE practice:
def test_update_table(test_setup):
    driver.get("https://sqlbolt.com/lesson/updating_rows")
    time.sleep(3)
    clearbutton = driver.find_element_by_xpath("//a[@class='clear']")
    clearbutton.click()
    text_field = driver.find_element_by_xpath("//textarea[@class='ace_text-input']")
    # question #1:
    text_field.send_keys("""update Movies set director = "John Lasseter" where title = "A Bug's Life"
    """)
    run_query_btn = driver.find_element_by_xpath("//a[@class='submit']")
    run_query_btn.click()
    time.sleep(3)
    # question #2:
    clearbutton.click()
    text_field.send_keys("""
    update Movies
    set year = "1999"
    where title = "Toy Story 2"
        """)
    run_query_btn.click()
    time.sleep(3)
    # question #3:
    clearbutton.click()
    text_field.send_keys(""" 
    update Movies
    set title = "Toy Story 3", director = "Lee Unkrich"
    where title = "Toy Story 8"
    """)
    run_query_btn.click()
    time.sleep(3)

# DELETE practice
def test_delete(test_setup):
    driver.get("https://sqlbolt.com/lesson/deleting_rows")
    time.sleep(3)
    clearbutton = driver.find_element_by_xpath("//a[@class='clear']")
    clearbutton.click()
    text_field = driver.find_element_by_xpath("//textarea[@class='ace_text-input']")
    # question #1:
    text_field.send_keys("""
    delete from Movies
    where year < 2005
        """)
    run_query_btn = driver.find_element_by_xpath("//a[@class='submit']")
    run_query_btn.click()
    time.sleep(3)
    # question #2:
    clearbutton.click()
    text_field.send_keys("""
    delete from movies
    where director = "Andrew Stanton"
    """)
    run_query_btn.click()
    time.sleep(3)

# INSERT practice
def test_insert(test_setup):
    driver.get("https://sqlbolt.com/lesson/inserting_rows")
    time.sleep(3)
    clearbutton = driver.find_element_by_xpath("//a[@class='clear']")
    clearbutton.click()
    text_field = driver.find_element_by_xpath("//textarea[@class='ace_text-input']")
    # question #1:
    text_field.send_keys("""
        INSERT INTO Movies VALUES (4, "Toy Story 4", "John Lasseter", "2002", 95)
           """)
    run_query_btn = driver.find_element_by_xpath("//a[@class='submit']")
    run_query_btn.click()
    time.sleep(3)
    # question #2:
    text_field.send_keys("""
    INSERT INTO Boxoffice VALUES (4, 8.7, 340000000, 270000000)
    """)
    run_query_btn.click()
    time.sleep(3)

# JOIN practice
def test_join(test_setup):
    driver.get("https://sqlbolt.com/lesson/select_queries_with_joins")
    time.sleep(3)
    clearbutton = driver.find_element_by_xpath("//a[@class='clear']")
    clearbutton.click()
    text_field = driver.find_element_by_xpath("//textarea[@class='ace_text-input']")
    # question #1:
    text_field.send_keys("""
    SELECT title, domestic_sales,international_sales FROM Movies
    JOIN Boxoffice on Id=Movie_Id
             """)
    time.sleep(3)
    # question #2:
    clearbutton.click()
    text_field.send_keys("""
        SELECT title, domestic_sales, international_sales FROM movies
        JOIN boxoffice ON id = movie_id
        WHERE international_sales > domestic_sales
                 """)
    time.sleep(3)
    # question #3:
    clearbutton.click()
    text_field.send_keys("""
    SELECT title, rating FROM movies
    JOIN boxoffice ON id=movie_id
    ORDER BY rating DESC
    """)
    time.sleep(3)