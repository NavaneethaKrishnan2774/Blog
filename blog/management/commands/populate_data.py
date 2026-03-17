from typing import Any
from blog.models import Post, Category
from django.core.management.base import BaseCommand
import random


class Command(BaseCommand):

    help = "this helps to insert the post data"

    def handle(self, *args: Any, **options: Any):

        Post.objects.all().delete()

        titles = [
        "Smart Public Transport Live Tracking and Notification System",
        "AI-Based Crowd Anomaly Detection Using Hybrid Deep Learning",
        "Intelligent Student Performance Prediction System",
        "Smart Attendance System Using Face Recognition",
        "Real-Time Traffic Congestion Prediction Using IoT and ML",
        "Blockchain-Based Secure Academic Certificate Verification System",
        "AI-Powered Healthcare Early Disease Prediction Platform",
        "Smart Waste Management System Using IoT Sensors",
        "Django-Based E-Commerce Platform with Personalized Recommendation Engine",
        "Swarm Intelligence-Based Emergency Evacuation Optimization System",
        "AI-Based Fake News Detection Using Natural Language Processing",
        "AI-Powered Resume Screening and Candidate Ranking System",
        "Deep Learning-Based Plant Disease Detection System",
        "AI-Based Road Accident Severity Prediction System",
        "AI-Powered Customer Sentiment Analysis Platform",
        "Predictive Maintenance System for Industrial Equipment Using Machine Learning",
        "AI-Based Phishing Website Detection System",
        "Smart Parking Management System Using IoT Sensors",
        "IoT-Based Water Quality Monitoring and Alert System",
        "Smart Street Lighting System Using Motion Detection and IoT",
        "AI-Based Flood Prediction and Early Warning System",
        "IoT-Based Air Pollution Monitoring and Prediction System",
        "Blockchain-Based Secure Voting System",
        "Blockchain-Based Land Registry and Property Management System",
        "Decentralized Identity Verification System Using Blockchain",
        "Secure File Sharing Platform Using Blockchain Technology",
        "AI-Based Network Intrusion Detection System",
        "AI-Powered Movie Recommendation System Using Collaborative Filtering",
        "Personalized Learning Recommendation System for Students",
        "Predictive Student Dropout Detection System Using Machine Learning",
        "Retail Demand Forecasting System Using Data Analytics",
        "Crime Prediction and Analysis System Using Machine Learning",
        "AI-Based Public Transport Demand Prediction System",
        "Smart Bus Arrival Time Prediction System Using GPS and Machine Learning",
        "Passenger Flow Analysis for Smart Public Transport Optimization",
        "AI-Based Public Transport Delay Prediction System",
        "Real-Time Bus Seat Availability Prediction System",
        "Smart Campus Navigation System Using Indoor Positioning",
        "AI-Powered Interview Preparation and Skill Assessment Platform",
        "Automated Meeting Notes Generator Using Speech Recognition and NLP"
        ]

        contents = [
        "An IoT-based transport monitoring system that uses GPS modules installed in buses to track real-time locations and provide ETA notifications to users.",
        "A surveillance system that detects abnormal crowd behavior using image segmentation and hybrid deep learning models to reduce false positives.",
        "A machine learning-based platform that predicts student academic performance using attendance, test scores, and behavioral data.",
        "A real-time face recognition system that automatically marks attendance and stores records in a centralized dashboard.",
        "A smart traffic monitoring system that analyzes sensor and CCTV data to predict congestion and suggest alternate routes.",
        "A blockchain-powered platform that securely stores and verifies academic certificates to prevent forgery.",
        "A healthcare prediction system that analyzes symptoms and medical history using classification algorithms for early disease detection.",
        "An IoT-enabled waste management system where smart bins detect fill levels and notify authorities for optimized collection.",
        "A Django-based e-commerce platform with a personalized recommendation engine using user behavior analysis.",
        "A swarm intelligence-based system that calculates optimal evacuation routes in crowded environments during emergencies.",
        "An AI-powered fake news detection system that analyzes news articles using natural language processing techniques to classify information as real or fake.",
        "An IoT-based smart parking system that detects available parking spaces using sensors and provides real-time availability updates through a mobile application.",
        "An AI-driven resume screening platform that automatically evaluates candidate resumes and ranks applicants based on skill matching and job requirements.",
        "An intelligent plant disease detection system that uses deep learning models to analyze leaf images and identify plant diseases at an early stage.",
        "An AI-based road accident prediction system that analyzes traffic patterns, weather conditions, and historical accident data to predict accident risks.",
        "A smart street lighting system using IoT sensors that automatically adjusts lighting intensity based on vehicle movement and environmental conditions.",
        "An AI-powered customer sentiment analysis platform that analyzes social media posts and reviews to understand customer opinions about products or services.",
        "An IoT-based air pollution monitoring system that collects environmental data using sensors and predicts pollution levels using machine learning models.",
        "A blockchain-based secure voting system that ensures transparency and prevents vote tampering through decentralized ledger technology.",
        "An AI-based intrusion detection system that monitors network traffic and identifies suspicious activities using machine learning algorithms.",
        "A machine learning-based retail demand forecasting system that predicts product demand using historical sales data and seasonal trends.",
        "An AI-powered chatbot system designed to provide automated customer support by understanding user queries using natural language processing.",
        "A smart campus navigation system that helps students locate classrooms, labs, and facilities using indoor positioning technologies.",
        "An AI-based phishing website detection system that analyzes website characteristics and identifies fraudulent websites to protect users.",
        "A real-time public transport delay prediction system that analyzes GPS and traffic data using machine learning to predict delays and notify passengers."
        ]

        img_urls = [
        "https://picsum.photos/id/1/800/400",
        "https://picsum.photos/id/2/800/400",
        "https://picsum.photos/id/3/800/400",
        "https://picsum.photos/id/4/800/400",
        "https://picsum.photos/id/5/800/400",
        "https://picsum.photos/id/6/800/400",
        "https://picsum.photos/id/7/800/400",
        "https://picsum.photos/id/8/800/400",
        "https://picsum.photos/id/9/800/400",
        "https://picsum.photos/id/10/800/400",
        "https://picsum.photos/id/11/800/400",
        "https://picsum.photos/id/12/800/400",
        "https://picsum.photos/id/13/800/400",
        "https://picsum.photos/id/14/800/400",
        "https://picsum.photos/id/15/800/400",
        "https://picsum.photos/id/16/800/400",
        "https://picsum.photos/id/17/800/400",
        "https://picsum.photos/id/18/800/400",
        "https://picsum.photos/id/19/800/400",
        "https://picsum.photos/id/20/800/400",
        "https://picsum.photos/id/21/800/400",
        "https://picsum.photos/id/22/800/400",
        "https://picsum.photos/id/23/800/400",
        "https://picsum.photos/id/24/800/400",
        "https://picsum.photos/id/25/800/400"
        ]

        categories = Category.objects.all()

        for title, content, img_url in zip(titles, contents, img_urls):
            category = random.choice(categories)

            Post.objects.create(title=title,content=content,img_url=img_url, category=category)

        self.stdout.write(self.style.SUCCESS("completed inserting datay"))
