import instaloader

insta = instaloader.Instaloader()
profil = input("Kullanıcı adı: ")

insta.download_profile(profil, profile_pic_only=True)
