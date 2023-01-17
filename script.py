from selenium import webdriver
import query
import email_sender

section_list = {}


def fetch():
    driver = webdriver.PhantomJS(
        'C://Users/Abdullah/Downloads/Compressed/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe')

    driver.get(
        'https://rds2.northsouth.edu/index.php/common/showofferedcourses')

    count = 0

    while True:
        matches = driver.find_elements_by_tag_name('tr')

        for match in matches:
            if 'Course' in match.text:
                continue
            temp_list = match.text.split()
            section_list[(temp_list[1], temp_list[2])] = temp_list

        next_page = driver.find_element_by_id('offeredCourseTbl_next')

        if int(next_page.get_attribute('tabindex')) == 0:
            next_page.click()
        else:
            break


while True:
    try:
        fetch()
        query_list = query.gen_query()
        message_list = []
        for i in range(len(query_list)):
            email = query_list[i][0]
            message = []
            for j in range(1, len(query_list[i])):
                for k in range(len(query_list[i][j])):
                    m = section_list.get((
                        query_list[i][j][k][0], query_list[i][j][k][1]))
                    if m == None:
                        continue
                    if int(m[-1]) > 0:
                        message.append(m)
            if message == []:
                continue
            message_list.append((email, message))

        email_sender.send_email(message_list)
        print('Email sent successfully')
    except Exception as e:
        print(e)
        continue
