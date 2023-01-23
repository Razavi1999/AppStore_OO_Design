from home_page import HomePage
from UserController import UserController
from SearchResultView import SearchResultView

applications = []
SRV = SearchResultView(applications)
hm = HomePage(SRV)

user_controller = UserController()
