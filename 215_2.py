from instapy import InstaPy

insta_username = '215_blackandwhite'
insta_password = 'kingmaker'

# set headless_browser=True if you want to run InstaPy on a server
try:
    session = InstaPy(
                      username=insta_username,
                      password=insta_password,
                      headless_browser=True,
                      multi_logs=True)
    session.login()
                      # settings
    session.set_upper_follower_count(limit=9999)
    session.set_do_follow(enabled=True, percentage=30, times=1)
    session.set_dont_unfollow_active_users(enabled=True, posts=1)
    session.set_smart_hashtags(['book', 'visitphilly', 'folkportraits'], limit=3, sort='top', log_tags=True)
                      # actions
    session.like_by_tags(['bookstagram', 'moodyports', 'philly', 'subjectivelyobjective'], amount=5, use_smart_hashtags=True)
    session.unfollow_users(amount=15, onlyNotFollowMe=True, sleep_delay=60)
    session.like_by_feed(amount=10, randomize=True, unfollow=False, interact=False)
    session.follow_user_following(['visitphilly', 'libraryofcongress', 'librarycompany', 'lifeinlit', 'phillylovenotes'], amount=10, randomize=True)
    session.like_by_locations(['214228753'], amount=15, skip_top_posts=True)
finally:
    # end the bot session
    session.end()
