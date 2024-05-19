import React from 'react';
import { Page, Text, View, Document, StyleSheet, Image, PDFViewer, Font } from '@react-pdf/renderer';
import logo from '../../assets/images/logo3.png';

const styles = StyleSheet.create({  
  page: {
    fontFamily: 'Helvetica',
    fontSize: 10,
    padding: 10,
    width: '60mm',
  },
  header: {
    textAlign: 'center',
    marginBottom: 10,
  },
  logo: {
    width: 150,
    height: 50,
    margin: '0 auto',
  },
  section: {
    marginBottom: 10,
  },
  bold: {
    fontWeight: 800,
  },
  table: {
    display: 'table',
    border: 'none'
  },
  tableRow: {
    flexDirection: 'row',
  },
  tableCol: {
    width: '33%',
    borderStyle: 'solid',
    borderWidth: 1,
    borderColor: '#000',
  },
  tableCell: {
    margin: 5,
    fontSize: 8,
  },
  footer: {
    textAlign: 'center',
    marginTop: 10,
  },
  textStrong: {
    fontWeight: 'bold',
    marginRight: 10
  }
});

const MyDocument = () => (
  <Document>
    <Page size="A4" style={styles.page}>
      <View style={styles.header}>
        <Image style={styles.logo} src={logo} />
        <Text>JVSoft</Text>
        <Text>Calle: HOLASOYVANESSA #12</Text>
        <Text>RFC: HOLAGRUPO12</Text>
        <Text>Tel: 3481468309</Text>
        <Text>Caja: Jesus Navarro</Text>
        <Text>Fecha: 17/11/2023 07:51 PM</Text>
        <Text>Recibo: #9</Text>
      </View>
      
      <View style={styles.table}>
        <View style={styles.tableRow}>
          <View style={styles.tableCol}>
            <Text style={styles.tableCell}>#</Text>
          </View>
          <View style={styles.tableCol}>
            <Text style={styles.tableCell}>Producto</Text>
          </View>
          <View style={styles.tableCol}>
            <Text style={styles.tableCell}>Precio</Text>
          </View>
          <View style={styles.tableCol}>
            <Text style={styles.tableCell}>Total</Text>
          </View>
        </View>
        <View style={styles.tableRow}>
          <View style={styles.tableCol}>
            <Text style={styles.tableCell}>1.0</Text>
          </View>
          <View style={styles.tableCol}>
            <Text style={styles.tableCell}>Coca cola 600ml</Text>
          </View>
          <View style={styles.tableCol}>
            <Text style={styles.tableCell}>$10.0</Text>
          </View>
          <View style={styles.tableCol}>
            <Text style={styles.tableCell}>$10.0</Text>
          </View>
        </View>
      </View>
      
      <View style={styles.section}>
        <Text>Total: $10.0</Text>
      </View>
      
      <View style={styles.footer}>
        <Text>Venta</Text>
        <Text>1</Text>
      </View>
          </Page>
  </Document>
);

const PDFTicket = () => (
  <PDFViewer style={{ width: '100%', height: '100vh' }}>
    <MyDocument />
  </PDFViewer>
);

export default PDFTicket;