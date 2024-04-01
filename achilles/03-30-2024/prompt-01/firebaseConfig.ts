// firebaseConfig.ts
export const db = {}; // Mock db object

// Mock collection function
export const collection = (db: any, collectionName: string) => {
  console.log(`Collection '${collectionName}' referenced.`);
  return {};
};

// Mock doc function for auto-ID generation
export const doc = (collectionRef: any) => {
  const autoId = `auto-id-${Math.random().toString(36).substring(2, 15)}`;
  console.log(`Document reference created with auto-generated ID: ${autoId}`);
  return { id: autoId };
};

// Mock setDoc function
export const setDoc = async (docRef: any, data: any) => {
  console.log(`Document ${docRef.id} set with data:`, data);
};

// Mock addDoc function
export const addDoc = async (collectionRef: any, data: any) => {
  const autoId = `auto-id-${Math.random().toString(36).substring(2, 15)}`;
  console.log(`Document added to collection with ID: ${autoId}, data:`, data);
  return { id: autoId };
};
