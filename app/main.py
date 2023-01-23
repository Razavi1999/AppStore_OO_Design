from home_page import HomePage
from user_controller import UserController
import datetime


if __name__ == '__main__':
    # initialize home page

    home_page = HomePage()
    print('home_page is available to handle your system')

    # initialize user controller
    user_controller = UserController()
    print('user_controller is available to handle your users')
    sedMahdi = user_controller.signUp('sedMahdi' , 'razavismhr@gmail.com' , '')


    category1 = home_page.add_category('cat1')
    category2 = home_page.add_category('cat2')
    category3 = home_page.add_category('cat3')

    home_page.display()

    advertisement1 = home_page.add_advertisement("iran man" , "")
    advertisement2 = home_page.add_advertisement("Zende Bad Iran" , "")
    advertisement3 = home_page.add_advertisement("Parjak" , "")

    home_page.display()

    app1 = category1.add_app('app1' , '1' , '2' , '3' ,'55' , '44' , '223' ,'66' , '77')
    app2 = category2.add_app('app2' , '77' , '88' , '92' ,'434' , '232' , '212' ,'343' , '212')
    app3 = category1.add_app('app3' , '1' , '2' , '3' ,'55' , '44' , '223' ,'66' , '77')
    app4 = category2.add_app('CafeBazar' , '1' , '2' , '3' ,'55' , '44' , '223' ,'66' , '77')
    app5 = category1.add_app('Snapp!' , '1' , '2' , '3' ,'55' , '44' , '223' ,'66' , '77')
    app6 = category2.add_app('SnappFood' , '1' , '2' , '3' ,'55' , '44' , '223' ,'66' , '77')

    app1.insert_comment(sedMahdi  , 'AAAA' , 'بسیار عالی بود'  ,  datetime.datetime.now())
    app2.insert_comment(sedMahdi , 'AAAB' , 'Excellent'  ,  datetime.datetime.now())

    home_page.search('Snapp!')

    app1.display()
