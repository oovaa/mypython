from pymongo import MongoClient
from pymongo.collection import Collection


def top_students(mongo_collection: Collection):
    students = mongo_collection.find()
    updated_students = []  # List to hold updated student documents with averageScore

    for stu in students:
        full_score = 0  # Reset full_score for each student
        topics = stu['topics']  # Access topics with correct syntax
        for topic in topics:
            full_score += topic['score']  # Access score with correct syntax

        # Calculate average and ensure floating-point division
        avg = full_score / len(topics)
        stu['averageScore'] = avg  # Add averageScore to the student document
        # Add updated student document to the list
        updated_students.append(stu)

    return updated_students  # Return the list of updated student documents
