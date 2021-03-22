from pprint import pprint
from var_dump import var_dump
import facebookinsights as fi
# quarter = page.posts.range(months=15).get()
# print(quarter)
# page.insights.lifetime('page_impressions').get()




#   dump(page.insights.daily(['page_impressions', 'page_fan_adds']).range(months=1).get())

if __name__ == '__main__':
    page = fi.authenticate(token='EAAbfTs6XFKwBAMZA0SbbHrqFSGNtmj4CVolgNKtYgyhsLiGWKXHreUxGyiXdOJ9uGm5vTa2XtbZAnZAZCCqbMXZCZBSLTVsh6I2M9YhgZBQT6Cf8gZBZBR1fCc9y110rAWoLiKZA93xJj5rIoZCwKlkY4QAYRwY4RK9x4q7JJjO2Eo742mXjF1iehDchUQP4MZCkpTSfT1tFUHUnuAZDZD')
    # page.insights.daily(['page_impressions', 'page_fan_adds']).range(months=1).get()
    # var_dump(page)
    # x = page.insights.daily(['page_impressions']).range(months=3).get()['page_impressions'][0]
    var_dump(page)

    # for xx in x:
    #     var_dump(xx)
    # var_dump(page)


# x = page.insights.daily(['page_impressions', 'page_fan_adds']).range(months=1).get()
# for xx in x:
#     pprint(xx)
# post.insights.lifetime('post_stories').get()
# for some, it's the other way around: no total, only the daily numbers
# for country_data in page.insights.daily('page_places_checkins_by_country'):
#     print(country_data)

# import facebookinsights as fi
# # this will launch a web browser to authenticate
# pages = fi.authenticate(
#     client_id='1934379426714796', 
#     client_secret='6e60400f1b6138abcdd9b7a78e0ed537', 
# )
# print(pages)
