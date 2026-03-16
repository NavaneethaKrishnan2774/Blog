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
        ]

        categories = Category.objects.all()

        for title, content, img_url in zip(titles, contents, img_urls):
            category = random.choice(categories)

            Post.objects.create(
                title=title,
                content=content,
                img_url=img_url,
                category=category
            )

        self.stdout.write(self.style.SUCCESS("completed inserting datay"))
