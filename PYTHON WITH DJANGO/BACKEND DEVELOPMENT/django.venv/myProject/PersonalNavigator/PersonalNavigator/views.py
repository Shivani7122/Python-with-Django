from django.shortcuts import render
from django.http import HttpResponse

def nav(rquest):
    s = '''<h2>Lecture Planner<br></h2>
    <a href="https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&pp=0gcJCbcEOCosWNin">Django by CWH</a><br>
    <a href="https://www.youtube.com/watch?v=QUX18Ba9cd8&list=PLu71SKxNbfoAMcPw8uJXxjeLwYQV8MkpQ">Chai with DSA (Hitesh Choudhary)</a><br>
    <a href="https://www.youtube.com/watch?v=K2QhLEzYBH8&list=PLsjpRo2EZP1K_glKX0lG6BkviJFxjuGls">Django by Mohit Decodes</a><br>
    <a href="https://www.youtube.com/watch?v=3obEP8eLsCw&pp=ygUQb3BlcmF0aW5nIHN5c3RlbQ%3D%3D">Operatin Systems by LoveBabbar</a><br>
    <a href="https://www.youtube.com/watch?v=dl00fOOYLOM&pp=ygUQZGJtcyBsb3ZlIGJhYmJhcg%3D%3D">DBMS by LoveBabbar</a><br>
    <a href="https://youtu.be/6l88XYUjNIs?si=OV_rAF8lWW6kkbqR">Cloud Computing by 5-Minutes Engineering</a><br>
    <a href="https://youtu.be/lFeYU31TnQ8?si=DOW4sQS6EaFP_BR-">System Design by Piyush Garg</a>'''
    return HttpResponse(s)