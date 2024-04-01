import { collection, doc, setDoc } from "./firebaseConfig";

import { db } from "./firebaseConfig"; // Replace with your Firebase config

async function addDocumentToCollection() {
  const collectionRef = collection(db, "myCollection"); // Replace "myCollection" with your collection name

  // Create a document reference with an auto-generated ID
  const docRef = doc(collectionRef);

  // Data to save
  const data = {
    name: "John Doe",
    age: 30,
  };

  try {
    await setDoc(docRef, data);
    console.log("Document added with ID:", docRef.id);
  } catch (error) {
    console.error("Error adding document:", error);
  }
}

addDocumentToCollection();