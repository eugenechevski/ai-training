import { db } from "./firebaseConfig"; // Replace with your Firebase config
import { collection, addDoc } from "./firebaseConfig";


// Your document data
const docData = {
  name: "Los Angeles",
  state: "CA",
  country: "USA"
};

async function addDocument() {
  try {
    // Add a new document with a generated id to a specified collection
    const docRef = await addDoc(collection(db, "cities"), docData);
    console.log("Document written with ID: ", docRef.id);
  } catch (e) {
    console.error("Error adding document: ", e);
  }
}

// Call the function to add the document
addDocument();