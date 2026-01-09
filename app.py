"""
Ruchika Mahajan - Portfolio with Fixed Image Loading
Complete Flask Application
"""

from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__, static_folder='static')

# Verify image exists
IMAGE_PATH = os.path.join(app.static_folder, 'images', 'profile.png')
if not os.path.exists(IMAGE_PATH):
    print(f"WARNING: Image not found at {IMAGE_PATH}")
    print("Please place your image at: static/images/profile.png")

# HTML Template with embedded CSS and JavaScript
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ruchika Mahajan | Data Science & AI Engineering</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    <style>
        /* Global Styles - Futuristic Dark Theme */
        :root {
            --neon-blue: #00f3ff;
            --neon-purple: #b967ff;
            --neon-pink: #ff2e7a;
            --dark-bg: #0a0a12;
            --darker-bg: #05050a;
            --card-bg: rgba(20, 20, 30, 0.7);
            --card-border: rgba(0, 243, 255, 0.2);
            --text-light: #ffffff;
            --text-glow: rgba(255, 255, 255, 0.9);
            --text-muted: #a0a0c0;
            --transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        html {
            scroll-behavior: smooth;
        }
        
        body {
            font-family: 'Inter', sans-serif;
            line-height: 1.6;
            color: var(--text-light);
            background: var(--dark-bg);
            overflow-x: hidden;
            background-image: 
                radial-gradient(circle at 20% 80%, rgba(0, 243, 255, 0.05) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(185, 103, 255, 0.05) 0%, transparent 50%);
        }
        
        h1, h2, h3, h4 {
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 600;
            margin-bottom: 1rem;
            background: linear-gradient(90deg, var(--neon-blue), var(--neon-purple));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .container {
            width: 90%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        .section {
            min-height: 100vh;
            padding: 120px 0;
            position: relative;
            overflow: hidden;
            opacity: 0;
            transform: translateY(50px);
            transition: opacity 1s ease, transform 1s ease;
        }
        
        .section.active {
            opacity: 1;
            transform: translateY(0);
        }
        
        .section-title {
            text-align: center;
            margin-bottom: 80px;
            position: relative;
        }
        
        .section-title h2 {
            font-size: 3.5rem;
            display: inline-block;
            position: relative;
            text-shadow: 0 0 20px rgba(0, 243, 255, 0.3);
        }
        
        .section-title h2:after {
            content: '';
            position: absolute;
            bottom: -15px;
            left: 50%;
            transform: translateX(-50%);
            width: 100px;
            height: 3px;
            background: linear-gradient(90deg, var(--neon-blue), var(--neon-purple));
            border-radius: 2px;
        }
        
        .section-title p {
            color: var(--text-muted);
            font-size: 1.2rem;
            max-width: 600px;
            margin: 25px auto 0;
        }
        
        /* Navigation - Fixed RM issue */
        .navbar {
            position: fixed;
            top: 0;
            width: 100%;
            background: rgba(10, 10, 18, 0.9);
            backdrop-filter: blur(15px);
            z-index: 1000;
            padding: 25px 0;
            transition: var(--transition);
            border-bottom: 1px solid rgba(0, 243, 255, 0.1);
        }
        
        .nav-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .logo {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 1.8rem;
            font-weight: 700;
            background: linear-gradient(90deg, var(--neon-blue), var(--neon-purple));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-decoration: none;
            text-shadow: 0 0 20px rgba(0, 243, 255, 0.3);
        }
        
        .logo-text {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 1.8rem;
            font-weight: 700;
            background: linear-gradient(90deg, var(--neon-blue), var(--neon-purple));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-decoration: none;
            text-shadow: 0 0 20px rgba(0, 243, 255, 0.3);
        }
        
        .nav-links {
            display: flex;
            list-style: none;
            gap: 35px;
        }
        
        .nav-links a {
            text-decoration: none;
            color: var(--text-muted);
            font-weight: 500;
            font-size: 1.1rem;
            transition: var(--transition);
            position: relative;
            padding: 8px 0;
        }
        
        .nav-links a:hover {
            color: var(--neon-blue);
        }
        
        .nav-links a.active {
            color: var(--neon-blue);
        }
        
        .nav-links a:after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 0;
            height: 2px;
            background: linear-gradient(90deg, var(--neon-blue), var(--neon-purple));
            transition: var(--transition);
        }
        
        .nav-links a:hover:after,
        .nav-links a.active:after {
            width: 100%;
        }
        
        /* Hero Section - Animated */
        #home {
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            background: radial-gradient(circle at center, rgba(0, 243, 255, 0.1) 0%, transparent 70%);
        }
        
        .hero-content {
            max-width: 900px;
            margin: 0 auto;
            position: relative;
            z-index: 2;
        }
        
        .profile-img-container {
            width: 280px;
            height: 280px;
            margin: 0 auto 40px;
            position: relative;
        }
        
 .profile-img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
    position: relative;
    z-index: 2;

    /* simple neon border */
    border: 4px solid var(--neon-blue);

    box-shadow:
        0 0 30px rgba(0, 243, 255, 0.4),
        0 0 60px rgba(185, 103, 255, 0.3);

    animation: float 6s ease-in-out infinite;
}

        
        .tagline {
            display: inline-block;
            font-size: 1.5rem;
            color: var(--neon-blue);
            margin-bottom: 30px;
            font-weight: 500;
            text-shadow: 0 0 10px rgba(0, 243, 255, 0.5);
        }
        
        .hero p {
            font-size: 1.3rem;
            color: var(--text-muted);
            margin-bottom: 40px;
            max-width: 700px;
            margin-left: auto;
            margin-right: auto;
            line-height: 1.8;
        }
        
        .cta-buttons {
            display: flex;
            gap: 25px;
            justify-content: center;
            margin-top: 40px;
        }
        
        .btn {
            display: inline-flex;
            align-items: center;
            gap: 12px;
            padding: 18px 40px;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            font-size: 1.1rem;
            transition: var(--transition);
            position: relative;
            overflow: hidden;
            border: none;
            cursor: pointer;
        }
        
        .btn:before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
            transition: 0.8s;
        }
        
        .btn:hover:before {
            left: 100%;
        }
        
        .btn-primary {
            background: linear-gradient(45deg, var(--neon-blue), var(--neon-purple));
            color: white;
            box-shadow: 0 10px 30px rgba(0, 243, 255, 0.3);
        }
        
        .btn-primary:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(0, 243, 255, 0.4);
        }
        
        .btn-secondary {
            background: transparent;
            color: var(--neon-blue);
            border: 2px solid var(--neon-blue);
        }
        
        .btn-secondary:hover {
            background: rgba(0, 243, 255, 0.1);
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0, 243, 255, 0.2);
        }
        
        /* About Section - Grid Layout */
        #about {
            background: linear-gradient(180deg, var(--dark-bg) 0%, var(--darker-bg) 100%);
        }
        
        .about-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 40px;
            margin-top: 60px;
        }
        
        .about-card {
            background: var(--card-bg);
            backdrop-filter: blur(10px);
            border: 1px solid var(--card-border);
            border-radius: 20px;
            padding: 40px;
            transition: var(--transition);
            position: relative;
            overflow: hidden;
        }
        
        .about-card:before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, var(--neon-blue), var(--neon-purple));
            transform: scaleX(0);
            transition: transform 0.5s ease;
        }
        
        .about-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0, 243, 255, 0.1);
        }
        
        .about-card:hover:before {
            transform: scaleX(1);
        }
        
        .about-card h3 {
            font-size: 1.8rem;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        .about-card h3 i {
            font-size: 2rem;
        }
        
        .about-card p {
            color: var(--text-muted);
            line-height: 1.8;
            margin-bottom: 25px;
        }
        
        .skill-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            margin-top: 20px;
        }
        
        .skill-tag {
            padding: 10px 20px;
            background: rgba(0, 243, 255, 0.1);
            border: 1px solid rgba(0, 243, 255, 0.3);
            border-radius: 25px;
            color: var(--neon-blue);
            font-size: 0.9rem;
            font-weight: 500;
            transition: var(--transition);
        }
        
        .skill-tag:hover {
            background: rgba(0, 243, 255, 0.2);
            transform: translateY(-3px);
        }
        
        /* Experience Section - Timeline */
        #experience {
            background: linear-gradient(180deg, var(--darker-bg) 0%, var(--dark-bg) 100%);
        }
        
        .timeline {
            position: relative;
            max-width: 1000px;
            margin: 60px auto 0;
        }
        
        .timeline:before {
            content: '';
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            top: 0;
            bottom: 0;
            width: 2px;
            background: linear-gradient(180deg, var(--neon-blue), var(--neon-purple));
        }
        
        .timeline-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 80px;
            opacity: 0;
            transform: translateY(30px);
            transition: opacity 0.8s ease, transform 0.8s ease;
        }
        
        .timeline-item.visible {
            opacity: 1;
            transform: translateY(0);
        }
        
        .timeline-item:nth-child(odd) {
            flex-direction: row;
        }
        
        .timeline-item:nth-child(even) {
            flex-direction: row-reverse;
        }
        
        .timeline-content {
            width: 45%;
            background: var(--card-bg);
            backdrop-filter: blur(10px);
            border: 1px solid var(--card-border);
            border-radius: 20px;
            padding: 35px;
            position: relative;
            transition: var(--transition);
        }
        
        .timeline-content:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0, 243, 255, 0.1);
        }
        
        .timeline-content:before {
            content: '';
            position: absolute;
            top: 30px;
            width: 20px;
            height: 20px;
            background: var(--neon-blue);
            border-radius: 50%;
            box-shadow: 0 0 20px var(--neon-blue);
        }
        
        .timeline-item:nth-child(odd) .timeline-content:before {
            right: -60px;
        }
        
        .timeline-item:nth-child(even) .timeline-content:before {
            left: -60px;
        }
        
        .timeline-content h3 {
            font-size: 1.6rem;
            margin-bottom: 10px;
        }
        
        .timeline-content .company {
            color: var(--neon-purple);
            font-weight: 600;
            margin-bottom: 10px;
            font-size: 1.2rem;
        }
        
        .timeline-content .duration {
            color: var(--text-muted);
            font-size: 1rem;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .timeline-content ul {
            list-style: none;
            padding-left: 0;
        }
        
        .timeline-content li {
            color: var(--text-muted);
            margin-bottom: 12px;
            padding-left: 25px;
            position: relative;
            line-height: 1.6;
        }
        
        .timeline-content li:before {
            content: '▸';
            position: absolute;
            left: 0;
            color: var(--neon-blue);
        }
        
        /* Projects Section - Grid with Hover */
        #projects {
            background: linear-gradient(180deg, var(--dark-bg) 0%, var(--darker-bg) 100%);
        }
        
        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 40px;
            margin-top: 60px;
        }
        
        .project-card {
            background: var(--card-bg);
            backdrop-filter: blur(10px);
            border: 1px solid var(--card-border);
            border-radius: 20px;
            overflow: hidden;
            transition: var(--transition);
            position: relative;
        }
        
        .project-card:hover {
            transform: translateY(-15px);
            box-shadow: 0 30px 60px rgba(0, 243, 255, 0.15);
        }
        
        .project-card:before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, var(--neon-blue), var(--neon-purple));
        }
        
        .project-header {
            height: 180px;
            background: linear-gradient(45deg, rgba(0, 243, 255, 0.1), rgba(185, 103, 255, 0.1));
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 3.5rem;
            color: var(--neon-blue);
        }
        
        .project-content {
            padding: 35px;
        }
        
        .project-content h3 {
            font-size: 1.8rem;
            margin-bottom: 15px;
        }
        
        .project-features {
            background: rgba(0, 243, 255, 0.05);
            border-left: 3px solid var(--neon-blue);
            padding: 20px;
            margin: 20px 0;
            border-radius: 0 10px 10px 0;
        }
        
        .project-features h4 {
            color: var(--neon-blue);
            margin-bottom: 10px;
            font-size: 1.2rem;
        }
        
        .project-features ul {
            list-style: none;
            padding-left: 0;
        }
        
        .project-features li {
            color: var(--text-muted);
            margin-bottom: 8px;
            padding-left: 20px;
            position: relative;
        }
        
        .project-features li:before {
            content: '✓';
            position: absolute;
            left: 0;
            color: var(--neon-blue);
        }
        
        .project-content p {
            color: var(--text-muted);
            line-height: 1.7;
            margin-bottom: 25px;
        }
        
        .project-tech {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 20px;
        }
        
        .tech-tag {
            padding: 8px 16px;
            background: rgba(0, 243, 255, 0.1);
            border: 1px solid rgba(0, 243, 255, 0.3);
            border-radius: 20px;
            color: var(--neon-blue);
            font-size: 0.85rem;
            font-weight: 500;
        }
        
        /* Education Section */
        #education {
            background: linear-gradient(180deg, var(--darker-bg) 0%, var(--dark-bg) 100%);
        }
        
        .education-cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-top: 60px;
        }
        
        .education-card {
            background: var(--card-bg);
            backdrop-filter: blur(10px);
            border: 1px solid var(--card-border);
            border-radius: 20px;
            padding: 35px;
            text-align: center;
            transition: var(--transition);
            position: relative;
            overflow: hidden;
        }
        
        .education-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0, 243, 255, 0.1);
        }
        
        .education-card:before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, var(--neon-blue), var(--neon-purple));
        }
        
        .education-icon {
            width: 70px;
            height: 70px;
            background: linear-gradient(45deg, var(--neon-blue), var(--neon-purple));
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 25px;
            color: white;
            font-size: 1.8rem;
            box-shadow: 0 0 30px rgba(0, 243, 255, 0.3);
        }
        
        .education-card h3 {
            font-size: 1.5rem;
            margin-bottom: 10px;
        }
        
        .education-card .institution {
            color: var(--neon-purple);
            font-weight: 600;
            margin-bottom: 15px;
            font-size: 1.1rem;
        }
        
        .education-info {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
            flex-wrap: wrap;
        }
        
        .education-score {
            padding: 8px 20px;
            background: rgba(0, 243, 255, 0.1);
            border: 1px solid rgba(0, 243, 255, 0.3);
            border-radius: 20px;
            color: var(--neon-blue);
            font-weight: 600;
        }
        
        .education-year {
            padding: 8px 20px;
            background: rgba(185, 103, 255, 0.1);
            border: 1px solid rgba(185, 103, 255, 0.3);
            border-radius: 20px;
            color: var(--neon-purple);
            font-weight: 600;
        }
        
        /* Contact Section */
        #contact {
            background: linear-gradient(180deg, var(--dark-bg) 0%, var(--darker-bg) 100%);
        }
        
        .contact-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 40px;
            margin-top: 60px;
        }
        
        .contact-card {
            background: var(--card-bg);
            backdrop-filter: blur(10px);
            border: 1px solid var(--card-border);
            border-radius: 20px;
            padding: 35px;
            text-align: center;
            transition: var(--transition);
        }
        
        .contact-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0, 243, 255, 0.1);
        }
        
        .contact-icon {
            width: 70px;
            height: 70px;
            background: linear-gradient(45deg, var(--neon-blue), var(--neon-purple));
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 25px;
            color: white;
            font-size: 1.8rem;
            box-shadow: 0 0 30px rgba(0, 243, 255, 0.3);
        }
        
        .contact-card h3 {
            font-size: 1.5rem;
            margin-bottom: 15px;
        }
        
        .contact-card p {
            color: var(--text-muted);
            margin-bottom: 15px;
            line-height: 1.6;
        }
        
        .contact-link {
            color: var(--neon-blue);
            text-decoration: none;
            font-weight: 500;
            transition: var(--transition);
            display: inline-block;
            margin-top: 10px;
        }
        
        .contact-link:hover {
            color: var(--neon-purple);
            text-decoration: underline;
        }
        
        .social-links {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 40px;
        }
        
        .social-link {
            width: 55px;
            height: 55px;
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--neon-blue);
            font-size: 1.4rem;
            text-decoration: none;
            transition: var(--transition);
        }
        
        .social-link:hover {
            background: linear-gradient(45deg, var(--neon-blue), var(--neon-purple));
            color: white;
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0, 243, 255, 0.3);
        }
        
        /* Footer */
        .footer {
            background: rgba(5, 5, 10, 0.9);
            backdrop-filter: blur(10px);
            border-top: 1px solid var(--card-border);
            padding: 40px 0;
            text-align: center;
        }
        
        .footer p {
            color: var(--text-muted);
            font-size: 1rem;
            margin: 10px 0;
        }
        
        /* Animations */
        @keyframes float {
            0%, 100% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-20px);
            }
        }
        
        @keyframes rotate {
            from {
                transform: rotate(0deg);
            }
            to {
                transform: rotate(360deg);
            }
        }
        
        @keyframes pulse {
            0%, 100% {
                opacity: 1;
            }
            50% {
                opacity: 0.7;
            }
        }
        
        /* Responsive Design */
        @media (max-width: 992px) {
            .hero h1 {
                font-size: 3rem;
            }
            
            .section-title h2 {
                font-size: 2.5rem;
            }
            
            .profile-img-container {
                width: 220px;
                height: 220px;
            }
            
            .timeline:before {
                left: 30px;
            }
            
            .timeline-item {
                flex-direction: row !important;
                justify-content: flex-start;
            }
            
            .timeline-content {
                width: calc(100% - 80px);
                margin-left: 80px;
            }
            
            .timeline-content:before {
                left: -60px !important;
                right: auto !important;
            }
        }
        
        @media (max-width: 768px) {
            .nav-links {
                display: none;
            }
            
            .hero {
                padding-top: 100px;
            }
            
            .hero h1 {
                font-size: 2.5rem;
            }
            
            .section {
                padding: 80px 0;
            }
            
            .profile-img-container {
                width: 200px;
                height: 200px;
            }
            
            .cta-buttons {
                flex-direction: column;
                align-items: center;
                gap: 15px;
            }
            
            .btn {
                width: 100%;
                max-width: 300px;
                justify-content: center;
            }
        }
        
        @media (max-width: 480px) {
            .hero h1 {
                font-size: 2rem;
            }
            
            .section-title h2 {
                font-size: 2rem;
            }
            
            .tagline {
                font-size: 1.2rem;
            }
            
            .hero p {
                font-size: 1.1rem;
            }
        }
    </style>
</head>
<body>
    <!-- Navigation - Fixed RM issue -->
    <nav class="navbar" id="navbar">
        <div class="container nav-container">
            <a href="#home" class="logo-text"></a>
            <ul class="nav-links">
                <li><a href="#home" class="nav-link active">Home</a></li>
                <li><a href="#about" class="nav-link">About</a></li>
                <li><a href="#experience" class="nav-link">Experience</a></li>
                <li><a href="#projects" class="nav-link">Projects</a></li>
                <li><a href="#education" class="nav-link">Education</a></li>
                <li><a href="#contact" class="nav-link">Contact</a></li>
            </ul>
        </div>
    </nav>

    <!-- Hero Section -->
    <section id="home" class="section active">
        <div class="container">
            <div class="hero-content">
                <div class="profile-img-container">
<img src="/static/images/profile.png?v=1" alt="Ruchika Mahajan" class="profile-img" 
     onerror="this.src='https://images.unsplash.com/photo-1580489944761-15a19d654956?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80'">                </div>
                <span class="tagline">Data Science, Analyst, Web Developer & AI Engineering</span>
                <h1>Ruchika Mahajan</h1>
                <p>Dual-degree student at BITS Pilani specializing in Mathematics and Electrical & Electronics Engineering. Expertise in data science, financial analytics, and AI/ML systems for data-driven decision making.</p>
                <div class="cta-buttons">
                    <a href="#projects" class="btn btn-primary">
                        <i class="fas fa-code"></i> View Projects
                    </a>
                    <a href="#contact" class="btn btn-secondary">
                        <i class="fas fa-envelope"></i> Contact Me
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="section">
        <div class="container">
            <div class="section-title">
                <h2>About Me</h2>
                <p>Analytical mind with expertise in data science and AI engineering</p>
            </div>
            <div class="about-grid">
                <div class="about-card">
                    <h3><i class="fas fa-brain"></i> Data Science</h3>
                    <p>Specializing in statistical analysis, predictive modeling, and data visualization for complex business problems. Experienced in Python, R, SQL, and Power BI.</p>
                    <div class="skill-tags">
                        <span class="skill-tag">Python</span>
                        <span class="skill-tag">R</span>
                        <span class="skill-tag">SQL</span>
                        <span class="skill-tag">Power BI</span>
                        <span class="skill-tag">Statistical Analysis</span>
                        <span class="skill-tag">Data Visualization</span>
                    </div>
                </div>
                
                <div class="about-card">
                    <h3><i class="fas fa-robot"></i> AI & Machine Learning</h3>
                    <p>Developing and deploying machine learning models for financial analysis, natural language processing, and computer vision applications.</p>
                    <div class="skill-tags">
                        <span class="skill-tag">TensorFlow</span>
                        <span class="skill-tag">PyTorch</span>
                        <span class="skill-tag">NLP</span>
                        <span class="skill-tag">Computer Vision</span>
                        <span class="skill-tag">OpenCV</span>
                        <span class="skill-tag">Predictive Analytics</span>
                    </div>
                </div>
                
                <div class="about-card">
                    <h3><i class="fas fa-chart-line"></i> Financial Analytics</h3>
                    <p>Expertise in financial modeling, risk analysis, and algorithmic trading systems. Experience with quantitative analysis and financial data pipelines.</p>
                    <div class="skill-tags">
                        <span class="skill-tag">Financial Modeling</span>
                        <span class="skill-tag">Risk Analysis</span>
                        <span class="skill-tag">Algorithmic Trading</span>
                        <span class="skill-tag">Quantitative Analysis</span>
                        <span class="skill-tag">Time Series</span>
                        <span class="skill-tag">Market Analysis</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Experience Section -->
    <section id="experience" class="section">
        <div class="container">
            <div class="section-title">
                <h2>Experience</h2>
                <p>Professional journey in data science and analytics</p>
            </div>
            <div class="timeline">
                <div class="timeline-item">
                    <div class="timeline-content">
                        <h3>Strategy and Transaction Analytics Intern</h3>
                        <div class="company">EY Parthenon</div>
                        <div class="duration"><i class="far fa-calendar"></i> July 2025 - December 2025</div>
                        <ul>
                            <li>Strategic analytics for transaction advisory projects</li>
                            <li>Data-driven insights for business decisions</li>
                            <li>Analytical models for financial transactions</li>
                        </ul>
                    </div>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-content">
                        <h3>Software Developer (AI) Intern</h3>
                        <div class="company">Girl Power Talk</div>
                        <div class="duration"><i class="far fa-calendar"></i> July 2024 - August 2024</div>
                        <ul>
                            <li>Developed AI applications using C++ and Python</li>
                            <li>Achieved 20% system efficiency improvement</li>
                            <li>Designed ML pipelines improving speed by 15%</li>
                            <li>Enhanced scalability of AI/ML models</li>
                        </ul>
                    </div>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-content">
                        <h3>Data Analyst & Visualizations Intern</h3>
                        <div class="company">Servon Solutions</div>
                        <div class="duration"><i class="far fa-calendar"></i> May 2024 - June 2024</div>
                        <ul>
                            <li>Designed interactive dashboards using Power BI</li>
                            <li>Reduced manual effort by 40% through automation</li>
                            <li>Analyzed large datasets with SQL and Python</li>
                            <li>Created structured learning content using Canva</li>
                        </ul>
                    </div>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-content">
                        <h3>Web Developer</h3>
                        <div class="company">I Care Foundation, Mexico</div>
                        <div class="duration"><i class="far fa-calendar"></i> May 2023 - July 2023</div>
                        <ul>
                            <li>Developed responsive websites for social initiatives</li>
                            <li>Implemented frontend frameworks for UX optimization</li>
                            <li>Created accessible web interfaces</li>
                            <li>Collaborated with design teams</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="section">
        <div class="container">
            <div class="section-title">
                <h2>Projects</h2>
                <p>Innovative solutions in data science and AI</p>
            </div>
            <div class="projects-grid">
                <div class="project-card">
                    <div class="project-header">
                        <i class="fas fa-comment-dots"></i>
                    </div>
                    <div class="project-content">
                        <h3>Financial Analysis Chatbot</h3>
                        <p>AI-driven financial analysis chatbot with full UI implementation for automated financial reporting and analysis.</p>
                        
                        <div class="project-features">
                            <h4>UI/UX Features:</h4>
                            <ul>
                                <li>Interactive chat interface with real-time responses</li>
                                <li>Dashboard with financial metrics visualization</li>
                                <li>Dynamic chart generation for financial trends</li>
                                <li>Multi-language support interface</li>
                                <li>Responsive design for all devices</li>
                                <li>Dark/Light theme toggle</li>
                                <li>Export functionality for reports</li>
                            </ul>
                        </div>
                        
                        <div class="project-features">
                            <h4>Technical Features:</h4>
                            <ul>
                                <li>Generates P&L statements, balance sheets, income statements</li>
                                <li>Automated financial ratio analysis</li>
                                <li>NLP-driven query handling</li>
                                <li>Trend insights and predictive analytics</li>
                                <li>Real-time data processing</li>
                            </ul>
                        </div>
                        
                        <div class="project-tech">
                            <span class="tech-tag">Python</span>
                            <span class="tech-tag">Flask</span>
                            <span class="tech-tag">React</span>
                            <span class="tech-tag">NLP</span>
                            <span class="tech-tag">Pandas</span>
                            <span class="tech-tag">Chart.js</span>
                            <span class="tech-tag">REST API</span>
                        </div>
                    </div>
                </div>
                
                <div class="project-card">
                    <div class="project-header">
                        <i class="fas fa-chart-bar"></i>
                    </div>
                    <div class="project-content">
                        <h3>Power BI Conversational Analytics Chatbot</h3>
                        <p>Intelligent chatbot integrated with Power BI dashboards for natural-language business analytics.</p>
                        
                        <div class="project-features">
                            <h4>UI/UX Features:</h4>
                            <ul>
                                <li>Seamless Power BI dashboard integration</li>
                                <li>Voice-to-text input support</li>
                                <li>Interactive data exploration interface</li>
                                <li>Customizable dashboard views</li>
                                <li>Real-time notification system</li>
                                <li>Multi-user collaboration features</li>
                                <li>Mobile-responsive analytics interface</li>
                            </ul>
                        </div>
                        
                        <div class="project-features">
                            <h4>Technical Features:</h4>
                            <ul>
                                <li>Natural-language queries on KPIs and metrics</li>
                                <li>Real-time insight extraction from dashboards</li>
                                <li>Automated trend detection and summary generation</li>
                                <li>Multi-data source integration</li>
                                <li>Predictive analytics recommendations</li>
                            </ul>
                        </div>
                        
                        <div class="project-tech">
                            <span class="tech-tag">Power BI</span>
                            <span class="tech-tag">Python</span>
                            <span class="tech-tag">Power Automate</span>
                            <span class="tech-tag">Power Apps</span>
                            <span class="tech-tag">Azure</span>
                            <span class="tech-tag">JavaScript</span>
                            <span class="tech-tag">API Integration</span>
                        </div>
                    </div>
                </div>
                
                <div class="project-card">
                    <div class="project-header">
                        <i class="fas fa-chart-line"></i>
                    </div>
                    <div class="project-content">
                        <h3>ETF Time Series Analysis with Automated Reporting</h3>
                        <p>Comprehensive ETF analysis system with automated reporting and visualization.</p>
                        
                        <div class="project-features">
                            <h4>Key Features:</h4>
                            <ul>
                                <li>End-to-end R pipeline for time-series analysis</li>
                                <li>Automated HTML report generation via RMarkdown</li>
                                <li>Interactive visualizations with ggplot2</li>
                                <li>Technical indicators computation (SMA, RSI, etc.)</li>
                                <li>Log returns and volatility analysis</li>
                                <li>Portfolio optimization suggestions</li>
                            </ul>
                        </div>
                        
                        <div class="project-tech">
                            <span class="tech-tag">R</span>
                            <span class="tech-tag">ggplot2</span>
                            <span class="tech-tag">RMarkdown</span>
                            <span class="tech-tag">Quantmod</span>
                            <span class="tech-tag">Tidyverse</span>
                            <span class="tech-tag">Time Series</span>
                        </div>
                    </div>
                </div>
                
                <div class="project-card">
                    <div class="project-header">
                        <i class="fas fa-shield-alt"></i>
                    </div>
                    <div class="project-content">
                        <h3>Financial Data Pipeline with Anomaly Detection</h3>
                        <p>Automated financial data pipeline with real-time anomaly detection and visualization.</p>
                        
                        <div class="project-features">
                            <h4>Key Features:</h4>
                            <ul>
                                <li>Automated data fetching from Yahoo Finance</li>
                                <li>Z-score based anomaly detection</li>
                                <li>Real-time alert system for abnormal activities</li>
                                <li>Automated visualization and reporting</li>
                                <li>Historical data analysis</li>
                                <li>Custom threshold configuration</li>
                            </ul>
                        </div>
                        
                        <div class="project-tech">
                            <span class="tech-tag">Python</span>
                            <span class="tech-tag">Pandas</span>
                            <span class="tech-tag">NumPy</span>
                            <span class="tech-tag">yfinance</span>
                            <span class="tech-tag">Matplotlib</span>
                            <span class="tech-tag">Scikit-learn</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Education Section -->
    <section id="education" class="section">
        <div class="container">
            <div class="section-title">
                <h2>Education</h2>
                <p>Academic foundation in mathematics and engineering</p>
            </div>
            <div class="education-cards">
                <div class="education-card">
                    <div class="education-icon">
                        <i class="fas fa-graduation-cap"></i>
                    </div>
                    <h3>M.Sc. (Hons.) Mathematics</h3>
                    <div class="institution">BITS Pilani, Goa Campus</div>
                    <div class="education-info">
                        <span class="education-score">CGPA: 7.31</span>
                        <span class="education-year">Expected: 2026</span>
                    </div>
                </div>
                
                <div class="education-card">
                    <div class="education-icon">
                        <i class="fas fa-bolt"></i>
                    </div>
                    <h3>B.E. (Hons.) Electrical & Electronics Engineering</h3>
                    <div class="institution">BITS Pilani, Goa Campus</div>
                    <div class="education-info">
                        <span class="education-score">CGPA: 7.31</span>
                        <span class="education-year">Expected: 2026</span>
                    </div>
                </div>
                
                <div class="education-card">
                    <div class="education-icon">
                        <i class="fas fa-school"></i>
                    </div>
                    <h3>Class XII (CBSE)</h3>
                    <div class="institution">Delhi Public School, Paradip</div>
                    <div class="education-info">
                        <span class="education-score">97%</span>
                        <span class="education-year">2021</span>
                    </div>
                </div>
                
                <div class="education-card">
                    <div class="education-icon">
                        <i class="fas fa-award"></i>
                    </div>
                    <h3>Class X (CBSE)</h3>
                    <div class="institution">Delhi Public School, Panipat</div>
                    <div class="education-info">
                        <span class="education-score">96%</span>
                        <span class="education-year">2019</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="section">
        <div class="container">
            <div class="section-title">
                <h2>Contact</h2>
                <p>Let's connect for innovative solutions</p>
            </div>
            <div class="contact-grid">
                <div class="contact-card">
                    <div class="contact-icon">
                        <i class="fas fa-envelope"></i>
                    </div>
                    <h3>Email</h3>
                    
                    <a href="mailto:f20212532@goa.bits-pilani.ac.in" class="contact-link">
                        f20212532@goa.bits-pilani.ac.in
                    </a>
                </div>
                
                <div class="contact-card">
                    <div class="contact-icon">
                        <i class="fas fa-phone"></i>
                    </div>
                    <h3>Phone</h3>
                    
                    <a href="tel:+919729002208" class="contact-link">
                        +91 9729002208
                    </a>
                </div>
                
                <div class="contact-card">
                    <div class="contact-icon">
                        <i class="fas fa-map-marker-alt"></i>
                    </div>
                    <h3>Location</h3>
                    <p>India</p>
                
                </div>
            </div>
            
            <div class="social-links">
                <a href="https://www.linkedin.com/in/ruchika-mahajan-98ba9b22b/" target="_blank" class="social-link">
                    <i class="fab fa-linkedin-in"></i>
                </a>
                <a href="https://github.com/ruch-proj/Projects?tab=readme-ov-file#projects" target="_blank" class="social-link">
                    <i class="fab fa-github"></i>
                </a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <p>©Ruchika Mahajan. All rights reserved.</p>
            <p>Web Development •Data Science • AI Engineering • Financial Analytics</p>
        </div>
    </footer>

    <script>
        // Section Animation on Scroll
        const sections = document.querySelectorAll('.section');
        const navLinks = document.querySelectorAll('.nav-link');
        
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                    
                    // Update active nav link
                    const id = entry.target.getAttribute('id');
                    navLinks.forEach(link => {
                        link.classList.remove('active');
                        if (link.getAttribute('href') === `#${id}`) {
                            link.classList.add('active');
                        }
                    });
                    
                    // Animate timeline items
                    if (id === 'experience') {
                        const timelineItems = document.querySelectorAll('.timeline-item');
                        timelineItems.forEach((item, index) => {
                            setTimeout(() => {
                                item.classList.add('visible');
                            }, index * 300);
                        });
                    }
                }
            });
        }, observerOptions);
        
        sections.forEach(section => {
            observer.observe(section);
        });
        
        // Smooth scrolling for navigation
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                const targetId = this.getAttribute('href');
                if (targetId === '#') return;
                
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    // Update active nav link
                    navLinks.forEach(link => link.classList.remove('active'));
                    this.classList.add('active');
                    
                    // Scroll to section
                    window.scrollTo({
                        top: targetElement.offsetTop - 80,
                        behavior: 'smooth'
                    });
                }
            });
        });
        
        // Navbar background on scroll
        window.addEventListener('scroll', () => {
            const navbar = document.getElementById('navbar');
            if (window.scrollY > 100) {
                navbar.style.background = 'rgba(10, 10, 18, 0.95)';
                navbar.style.backdropFilter = 'blur(15px)';
            } else {
                navbar.style.background = 'rgba(10, 10, 18, 0.9)';
            }
        });
        
        // Initialize first section
        sections[0].classList.add('active');
        
        // Debug image loading
        window.addEventListener('load', () => {
            const img = document.querySelector('.profile-img');
            console.log('Image source:', img.src);
            console.log('Image natural dimensions:', img.naturalWidth, 'x', img.naturalHeight);
            
            if (img.naturalWidth === 0) {
                console.log('Image failed to load, trying different source...');
                // Try with cache busting
                img.src = '/static/images/profile.png?' + new Date().getTime();
            }
        });
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
else:
    # This is needed for Vercel
    application = app


    app.run(debug=True, port=5000)
