from authlib.integrations.flask_client import OAuth

oauth = OAuth()

def init_oauth(app):
    oauth.init_app(app)

    # Register Google OAuth client
    oauth.register(
        name='google',
        client_id=app.config['GOOGLE_CLIENT_ID'],
        client_secret=app.config['GOOGLE_CLIENT_SECRET'],
        authorize_url='https://accounts.google.com/o/oauth2/auth',
        access_token_url='https://accounts.google.com/o/oauth2/token',
        client_kwargs={
            'scope': 'openid profile email',
        }
    )

    # Register Facebook OAuth client
    oauth.register(
        name='facebook',
        client_id=app.config['FACEBOOK_CLIENT_ID'],
        client_secret=app.config['FACEBOOK_CLIENT_SECRET'],
        authorize_url='https://www.facebook.com/dialog/oauth',
        access_token_url='https://graph.facebook.com/oauth/access_token',
        client_kwargs={
            'scope': 'email',
        }
    )

    # Register Twitter OAuth client
    oauth.register(
        name='twitter',
        client_id=app.config['TWITTER_CLIENT_ID'],
        client_secret=app.config['TWITTER_CLIENT_SECRET'],
        authorize_url='https://api.twitter.com/oauth/authenticate',
        access_token_url='https://api.twitter.com/oauth/access_token',
        client_kwargs={
            'scope': 'email',
        }
    )

    # Register LinkedIn OAuth client
    oauth.register(
        name='linkedin',
        client_id=app.config['LINKEDIN_CLIENT_ID'],
        client_secret=app.config['LINKEDIN_CLIENT_SECRET'],
        authorize_url='https://www.linkedin.com/oauth/v2/authorization',
        access_token_url='https://www.linkedin.com/oauth/v2/accessToken',
        client_kwargs={
            'scope': 'r_liteprofile r_emailaddress',
        }
    )
