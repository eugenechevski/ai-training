import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';

// final FirebaseFirestore _firestore = FirebaseFirestore.instance;
// final CollectionReference _collectionRef = _firestore.collection('yourCollectionName');

class MyDocument {
  final String id; // Document ID
  final String title;
  final String description;

  MyDocument({required this.id, required this.title, required this.description});

  // Factory constructor to create an instance from a DocumentSnapshot
  factory MyDocument.fromSnapshot(DocumentSnapshot snapshot) {
    return MyDocument(
      id: snapshot.id,
      title: snapshot['title'],
      description: snapshot['description'],
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  List<MyDocument> _documents = []; // List to store documents
  bool _isLoading = true; // Flag to indicate data loading state

  @override
  void initState() {
    super.initState();
    _fetchData();
  }

  Future<void> _fetchData() async {
    setState(() {
      _isLoading = true; // Set loading state to true
    });

    try {
      final QuerySnapshot querySnapshot = await _collectionRef.get();
      _documents = querySnapshot.docs.map((doc) => MyDocument.fromSnapshot(doc)).toList();
    } catch (error) {
      print('Error fetching data: $error');
    } finally {
      setState(() {
        _isLoading = false; // Set loading state to false
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('My Collection List'),
      ),
      body: _isLoading
          ? Center(child: CircularProgressIndicator()) // Display progress indicator while loading
          : ListView.builder(
              itemCount: _documents.length,
              itemBuilder: (context, index) {
                final document = _documents[index];
                // Access document fields here
                return ListTile(
                  title: Text(document.title),
                  subtitle: Text(document.description),
                );
              },
            ),
    );
  }
}