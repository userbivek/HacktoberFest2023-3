import tweepy
import matplotlib.pyplot as plt

# Set up your Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Function to fetch follower count over time
def fetch_follower_growth(screen_name, num_days):
    follower_count = []
    dates = []

    for status in tweepy.Cursor(api.user_timeline, screen_name=screen_name).items(num_days):
        follower_count.append(status.user.followers_count)
        dates.append(status.created_at.date())

    return dates, follower_count

# Main program
if __name__ == "__main__":
    screen_name = "TwitterUsername"  # Replace with the Twitter username you want to analyze
    num_days = 30  # Set the number of days to track follower growth

    dates, follower_count = fetch_follower_growth(screen_name, num_days)

    # Plot follower growth
    plt.plot(dates, follower_count, marker='o', linestyle='-')
    plt.title(f'Follower Growth for @{screen_name}')
    plt.xlabel('Date')
    plt.ylabel('Follower Count')
    plt.grid(True)
    plt.show()
