import 'package:cloud_firestore/cloud_firestore.dart';

final firestore = FirebaseFirestore.instance;
final collectionReference = firestore.collection('yourCollectionName');

Future<void> getAllDocuments() async {
    try {
      final QuerySnapshot querySnapshot = await collectionReference.get();

      // Process the documents in the list
      final List<DocumentSnapshot> documents = querySnapshot.docs;
      for (final document in documents) {
        final data = document.data();
        // Access document data using its ID or field names
        print('Document ID: ${document.id}');
        print('Document data: $data');
      }
    } catch (error) {
      print('Error getting documents: $error');
    }
  }

Stream<QuerySnapshot> collectionStream = collectionReference.snapshots();

collectionStream.listen((QuerySnapshot querySnapshot) {
  final List<DocumentSnapshot> documents = querySnapshot.docs;
  for (final document in documents) {
    final data = document.data();
    // Access document data using its ID or field names
    print('Document ID: ${document.id}');
    print('Document data: $data');
  }
});