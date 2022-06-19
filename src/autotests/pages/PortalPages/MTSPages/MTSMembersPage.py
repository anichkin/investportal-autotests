from autotests.pages.base_page import BasePage

class MTSMembersPage(BasePage):
    PATH = '/moscow-technical-school/participants'
    TITLE = 'Участникам - Инвестиционный портал Москвы'
    HEADER_XPATH = '//*[@id="uid-portal"]/div/div[1]/div[3]/div[1]/div/div'
    HEADER = 'УЧАСТНИКИ И КУРАТОРЫ ПРОЕКТА'
    SUBTITLE_XPATH = '//*[@id="uid-portal"]/div/div[1]/div[3]/div[2]/div/div/p'
    SUBTITLE = 'Главным органом взаимодействия участников является Экспертный совет, в состав которого войдут ключевые представители промышленности, образовательных и научных организаций, ассоциаций и институтов развития, а также органов исполнительной власти города Москвы.'
    HEADER2_XPATH = '//*[@id="uid-portal"]/div/div[1]/div[3]/div[4]/div/div[1]/div'
    HEADER2 = 'РОЛИ И ЗАДАЧИ УЧАСТНИКОВ ЭКСПЕРТНОГО СОВЕТА'
    ROLE1 = '//*[@id="uid-portal"]/div/div[1]/div[3]/div[4]/div/div[2]/div[2]'
    ROLE2 = '//*[@id="uid-portal"]/div/div[1]/div[3]/div[4]/div/div[2]/div[3]'
    ROLE3 = '//*[@id="uid-portal"]/div/div[1]/div[3]/div[4]/div/div[2]/div[4]'
    ROLE4 = '//*[@id="uid-portal"]/div/div[1]/div[3]/div[4]/div/div[2]/div[5]'
    PROGRAM_BUTTON = '//*[@id="uid-portal"]/div/div[1]/div[2]/div/div/div/div/a'
