from typing import Any
from blog.models import blog,categories
from django.core.management.base import BaseCommand
import random




class Command(BaseCommand):
    help="this cammand was created to populate data into the database"
    def handle(self, *args: Any, **options: Any) :
        #deleting the existing database

        blog.objects.all().delete()
        
        titles = [
    "The Evolution of AI in Modern Healthcare",
    "The Impact of Climate Change on Global Food Security",
    "The Rise of Renewable Energy Solutions",
    "Blockchain Technology: Beyond Cryptocurrency",
    "Mental Health Awareness in the Digital Age",
    "The Future of Autonomous Vehicles",
    "The Role of Big Data in Business Decision-Making",
    "Cybersecurity Threats and How to Combat Them",
    "The Growing Importance of Sustainable Fashion",
    "Advancements in Space Exploration",
    "The Ethics of Genetic Engineering",
    "The Influence of Social Media on Public Opinion",
    "AI and the Future of Work",
    "The Benefits of Mindfulness and Meditation",
    "Challenges in Global Water Scarcity",
    "The Evolution of Smart Cities",
    "The Role of Education in Bridging Socioeconomic Gaps",
    "The Impact of 5G Technology on Communication",
    "The Future of E-commerce and Online Shopping",
    "The Role of Government in Environmental Protection"
]

        contents = [
    "Explore how AI is revolutionizing healthcare through advanced diagnostic tools, personalized treatment plans, and predictive analytics. Delve into the ethical implications and the potential of AI in addressing global health challenges.",
    "Analyze how climate change affects global food security, focusing on crop production, food distribution, and the socio-economic impacts on vulnerable communities.",
    "Discuss the rise of renewable energy solutions such as solar, wind, and hydropower, and how they are contributing to reducing carbon emissions and combating climate change.",
    "Examine how blockchain technology is being utilized beyond cryptocurrency, including applications in supply chain management, secure transactions, and data integrity.",
    "Highlight the importance of mental health awareness in the digital age, addressing the challenges posed by social media, online interactions, and the impact of technology on mental well-being.",
    "Explore the future of autonomous vehicles, their potential impact on transportation, urban planning, and the ethical dilemmas they present.",
    "Discuss how big data is transforming business decision-making processes, enabling companies to make data-driven decisions that lead to increased efficiency and profitability.",
    "Examine the latest cybersecurity threats, including data breaches, ransomware, and phishing attacks, and discuss strategies for individuals and organizations to protect themselves.",
    "Explore the growing importance of sustainable fashion, focusing on eco-friendly materials, ethical production practices, and the shift towards a more sustainable fashion industry.",
    "Discuss recent advancements in space exploration, including missions to Mars, the development of space tourism, and the future possibilities of space colonization.",
    "Examine the ethics of genetic engineering, particularly in the areas of gene editing, designer babies, and the potential risks and benefits to society.",
    "Discuss the influence of social media on public opinion, including how platforms like Twitter and Facebook shape political discourse and the spread of information.",
    "Explore the implications of AI and automation on the future of work, including potential job displacement, the creation of new roles, and the need for re-skilling.",
    "Discuss the benefits of mindfulness and meditation, particularly in reducing stress, improving mental clarity, and promoting overall well-being.",
    "Examine the challenges associated with global water scarcity, focusing on regions most affected and potential solutions for ensuring access to clean water.",
    "Explore the evolution of smart cities, including the integration of IoT, smart infrastructure, and data-driven governance to create more efficient and livable urban environments.",
    "Discuss the role of education in bridging socioeconomic gaps, focusing on access to quality education, the digital divide, and initiatives to promote equality.",
    "Examine the impact of 5G technology on communication, including faster internet speeds, improved connectivity, and the potential to revolutionize industries like healthcare and transportation.",
    "Discuss the future of e-commerce and online shopping, focusing on trends such as personalization, AI-driven recommendations, and the rise of mobile commerce.",
    "Examine the role of government in environmental protection, including policy initiatives, regulations, and the balance between economic growth and sustainability."
]


        image_urls = [
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
    "https://picsum.photos/id/20/800/400"]

        category=categories.objects.all()
        
        for title,content,img_url in zip(titles,contents,image_urls):
            
            Categories=random.choice(category)
            
            blog.objects.create(title=title,content=content,img_url=img_url,category=Categories)
            
        self.stdout.write(self.style.SUCCESS("successfully inserted"))
            
    
    
    