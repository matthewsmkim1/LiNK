

import 'package:flutter/material.dart';

class GroupList extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final double sizeX = MediaQuery
        .of(context)
        .size
        .width;
    final double sizeY = MediaQuery
        .of(context)
        .size
        .height;
    return Container(
      width: sizeX,
      height: sizeY,
      color: Colors.grey[300],
      child: ListView(
        children: showContacts(),
      ),
    );
  }
}

class Contact {
  String name;
  String subtitle;
  IconData icon;

  Contact(this.name, this.subtitle, this.icon);
}

List<Contact> populateContacts() {
  List<Contact> contacts = List<Contact>();

  List<String> names = ["Matt", "Ben", "George", "Kenny"];
  List<String> subs = ["the beast", "the coolguy", "the curious", "the crazy"];
  List<IconData> icons = [
    Icons.sentiment_very_satisfied,
    Icons.sentiment_very_dissatisfied,
    Icons.sentiment_neutral,
    Icons.sentiment_satisfied
  ];

  for (int i = 0; i < names.length; i++) {
    contacts.add(Contact(names[i], subs[i], icons[i]));
  }
  return contacts;
}

List<ListTile> showContacts() {
  List<Contact> contacts = populateContacts();
  for (int i = 0; i < 20; i++) {
    contacts.addAll(populateContacts());
  }

  List<ListTile> tiles = List<ListTile>();

  contacts.forEach((contact) {
    tiles.add(ListTile(
      title: Text(contact.name),
      subtitle: Text(contact.subtitle),
      leading: CircleAvatar(
        child: Icon(contact.icon),
        backgroundColor: Colors.indigo[300],
      ),
      trailing: Icon(Icons.keyboard_arrow_right),
      onTap: () => print("printed!"),
    ));
  });
  return tiles;
}
