import unittest
import datetime
from home_page import HomePage
from user_controller import UserController
from search_result_view import SearchResultView
from top_apps_view import TopAppsView
from type import Type

class TestHomePage(unittest.TestCase):
    """docstring for TestHomePage."""

    def test_categories(self):
        home_page = HomePage()
        user_controller = UserController()

        sedMahdi = user_controller.signUp('sedMahdi' , 'razavismhr@gmail.com' , '')

        category1 = home_page.add_category('cat1')
        category2 = home_page.add_category('cat2')
        category3 = home_page.add_category('cat3')

        self.assertEqual(len(home_page.categories) , 3)


    def test_advertisements(self):
        home_page = HomePage()

        category1 = home_page.add_category('cat1')
        category2 = home_page.add_category('cat2')
        category3 = home_page.add_category('cat3')

        advertisement1 = home_page.add_advertisement("iran man" , "")
        advertisement2 = home_page.add_advertisement("Zende Bad Iran" , "")
        advertisement3 = home_page.add_advertisement("Parjak" , "")

        self.assertEqual(len(home_page.advertisements) , 3)
        self.assertTrue(advertisement1 in home_page.advertisements)

    def test_add_applications(self):
        home_page = HomePage()

        category1 = home_page.add_category('cat1')
        category2 = home_page.add_category('cat2')
        category3 = home_page.add_category('cat3')

        user_controller = UserController()
        developer = user_controller.create_developer('developer1', '/img')

        app1 = category1.add_app('app1' , '/imgs/icon1.png' , '/img1' , '/t1' ,'55' , Type(1) , 0 , 10000 , developer)
        app2 = category2.add_app('app2' , '/imgs/icon2.png' , '/img1' , '/t1' ,'434' , Type(1) , 0 , 10000 , developer)
        app3 = category1.add_app('app3' , '/imgs/icon3.png' , '/img1' , '/t1' ,'55' , Type(1) , 0 , 10000 , developer)
        app4 = category2.add_app('CafeBazar' , '/imgs/icon4.png' , '/img1' , '/t1' ,'55' , Type(2) , 0 , 10000 , developer)
        app5 = category1.add_app('Snapp!' , '/imgs/icon5.png' , '/img1' , '/t1' ,'/t1' , Type(1) , 1000 , 10000 , developer)
        app6 = category2.add_app('SnappFood' , '/imgs/icon6.png' , '/img1' , '/t1' ,'55' , Type(2) , 0 , 10000 , developer)


    def test_insert_comment(self):
        home_page = HomePage()

        category1 = home_page.add_category('cat1')
        category2 = home_page.add_category('cat2')
        category3 = home_page.add_category('cat3')

        user_controller = UserController()
        print('user_controller is available to handle your users')
        sedMahdi = user_controller.signUp('sedMahdi' , 'razavismhr@gmail.com' , '')


        app1 = category1.add_app('app1' , '1' , '2' , '3' ,'55' , '44' , '223' ,'66' , '77')
        app2 = category2.add_app('app2' , '77' , '88' , '92' ,'434' , '232' , '212' ,'343' , '212')
        app3 = category1.add_app('app3' , '1' , '2' , '3' ,'55' , '44' , '223' ,'66' , '77')
        app4 = category2.add_app('CafeBazar' , '1' , '2' , '3' ,'55' , '44' , '223' ,'66' , '77')
        app5 = category1.add_app('Snapp!' , '1' , '2' , '3' ,'55' , '44' , '223' ,'66' , '77')
        app6 = category2.add_app('SnappFood' , '1' , '2' , '3' ,'55' , '44' , '223' ,'66' , '77')

        app1.insert_comment(sedMahdi   , 'بسیار عالی بود'  ,  datetime.datetime.now())
        app2.insert_comment(sedMahdi  , 'Excellent'  ,  datetime.datetime.now())
        app3.insert_comment(sedMahdi  , 'Awful' , datetime.datetime.now())

        self.assertEqual(app1.comments[0].description , 'بسیار عالی بود')
        self.assertEqual(app2.comments[0].description , 'Excellent')
        self.assertEqual(app3.comments[0].description , 'Awful')
        self.assertTrue(len(app1.comments) > 0)


    def test_delete_comment(self):
        home_page = HomePage()

        category1 = home_page.add_category('cat1')
        category2 = home_page.add_category('cat2')
        category3 = home_page.add_category('cat3')

        user_controller = UserController()
        print('user_controller is available to handle your users')
        sedMahdi = user_controller.signUp('SedMahdi' , 'razavismhr@gmail.com' , '')
        Mojtaba = user_controller.signUp('Mojtaba' , 'mojtabaSafari@gmail.com' , '')
        MohamadReza = user_controller.signUp('MohammadReza' , 'mirshamsi@gmail.com' , '')

        app1 = category1.add_app('app1' , '1' , '2' , '3' ,'55' , '44' , '223' ,'66' , '77')
        app2 = category2.add_app('app2' , '77' , '88' , '92' ,'434' , '232' , '212' ,'343' , '212')
        app3 = category1.add_app('app3' , '1' , '2' , '3' ,'55' , '44' , '223' ,'66' , '77')
        app4 = category2.add_app('CafeBazar' , '1' , '2' , '3' ,'55' , '44' , '223' ,'66' , '77')
        app5 = category1.add_app('Snapp!' , '1' , '2' , '3' ,'55' , '44' , '223' ,'66' , '77')
        app6 = category2.add_app('SnappFood' , '1' , '2' , '3' ,'55' , '44' , '223' ,'66' , '77')

        app1.insert_comment(sedMahdi   , 'بسیار عالی بود'  ,  datetime.datetime.now())
        app1.insert_comment(Mojtaba  , 'Khob bod' , datetime.datetime.now())
        app2.insert_comment(sedMahdi , 'Excellent'  ,  datetime.datetime.now())
        app3.insert_comment(sedMahdi , 'Awful' , datetime.datetime.now())

        app1.delete_comment('Khob bod')
        print([c.description for c in app1.comments])

        for each in app1.comments:
            print(each.description)

        self.assertEqual(len(app1.comments) , 1)
        self.assertEqual(len(app2.comments) , 1)
        self.assertEqual(len(app3.comments) , 1)


    def test_search(self):
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

        app1.insert_comment(sedMahdi   , 'بسیار عالی بود'  ,  datetime.datetime.now())
        app2.insert_comment(sedMahdi  , 'Excellent'  ,  datetime.datetime.now())

        actual = home_page.search('Snapp!')
        self.assertEqual(actual[0] , app5)

    def test_top_apps_view(self):
        home_page = HomePage()
        print('home_page is available to handle your system')

        # initialize user controller
        user_controller = UserController()
        print('user_controller is available to handle your users')

        sedMahdi = user_controller.signUp('sedMahdi' , 'razavismhr@gmail.com' , '')
        Mojtaba = user_controller.signUp('Mojtaba' , 'mojtabaSafari@gmail.com' , '')
        MohamadReza = user_controller.signUp('MohammadReza' , 'mirshamsi@gmail.com' , '')


        category1 = home_page.add_category('cat1')
        category2 = home_page.add_category('cat2')
        category3 = home_page.add_category('cat3')

        home_page.display()

        advertisement1 = home_page.add_advertisement("iran man" , "")
        advertisement2 = home_page.add_advertisement("Zende Bad Iran" , "")
        advertisement3 = home_page.add_advertisement("Parjak" , "")

        home_page.display()

        app1 = category1.add_app('app1' , '1' , '2' , '3' ,'55' , '44' , '223' ,'66' , '77')
        app2 = category2.add_app('S_app2' , '77' , '88' , '92' ,'434' , '232' , '212' ,'343' , '212')
        app3 = category1.add_app('S_app3' , '1' , '2' , '3' ,'55' , '44' , '223' ,'66' , '77')
        app4 = category2.add_app('SCafeBazar' , '1' , '2' , '3' ,'55' , '44' , '223' ,'66' , '77')
        app5 = category1.add_app('Snapp!' , '1' , '2' , '3' ,'55' , '44' , '223' ,'66' , '77')
        app6 = category2.add_app('SnappFood' , '1' , '2' , '3' ,'55' , '44' , '223' ,'66' , '77')

        app1.insert_comment(sedMahdi   , 'بسیار عالی بود'  ,  datetime.datetime.now())
        app2.insert_comment(sedMahdi  , 'Excellent'  ,  datetime.datetime.now())


        search_result_view = SearchResultView()
        categories = [category1 , category2 , category3]

        search_result_view.search(categories , 'S')
        search_result_view.appPressHandler(0 , sedMahdi)
        search_result_view.appPressHandler(0 , Mojtaba)
        search_result_view.appPressHandler(0 , MohamadReza)
        search_result_view.appPressHandler(1 , sedMahdi)
        search_result_view.appPressHandler(2 , sedMahdi)
        search_result_view.appPressHandler(3 , Mojtaba)
        search_result_view.appPressHandler(3 , MohamadReza)

        top_apps_view = TopAppsView()
        top_apps_view.insert_application(categories)

        self.assertFalse(app2 in top_apps_view.applications)



if __name__ == '__main__':
    unittest.main()
