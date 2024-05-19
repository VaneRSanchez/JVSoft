import React, { useEffect, useState } from 'react';
import { useLocation, useNavigate } from "react-router-dom";
import { Page, Text, View, Document, StyleSheet, Image, PDFViewer, Font } from '@react-pdf/renderer';
import { v4 as uuidv4 } from 'uuid';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTimesCircle } from '@fortawesome/free-solid-svg-icons';
import logo from '../../assets/images/logo3.png';
import configData from '../../config.json';
import axios from 'axios';
import Alert from '../Alert';


const PDFTicket = ({ newModal, removeModal, newAlert, removeAlert }) => {
  const [ data, setData ] = useState(null);
  const location = useLocation();
  const navigate = useNavigate(); 

  useEffect(() => {
      const searchParams = new URLSearchParams(location.search);
      const sale_id = searchParams.get('id');
      if(!sale_id){
          navigate('/')
          return; 
      }

      const fetchData = async() => {
          const authToken = localStorage.getItem('authToken');
          const resp = await axios.get(`${configData.api_url}/sales`, 
          { 
            params: {
              query: 'obj', 
              id: sale_id
            },
            headers: {
                'Authorization': `Bearer ${authToken}`
            }
          });
          const resp_data = resp.data;

          const alert_id = uuidv4();
          if(!resp_data.success){    
              newAlert({
                  'id': alert_id,
                  'alert': <Alert key={alert_id} id={alert_id} title={<><FontAwesomeIcon icon={faTimesCircle} /> Error!</>} body={resp_data.msg} color={'danger'} removeAlert={removeAlert} timeout={3000} />
              });
              return;
          }
          setData(resp_data.data);
      };
      
      fetchData();
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  Font.register({
    family: 'Poppins',
    fonts: [
      { src: require('../../assets/fonts/Poppins/Poppins-Regular.ttf'), fontWeight: 'normal' },
      { src: require('../../assets/fonts/Poppins/Poppins-SemiBold.ttf'), fontWeight: 600 },
      { src: require('../../assets/fonts/Poppins/Poppins-Bold.ttf'), fontWeight: 700 },
      { src: require('../../assets/fonts/Poppins/Poppins-ExtraBold.ttf'), fontWeight: 800 },
    ]
  });

  const styles = StyleSheet.create({  
    page: {
      fontFamily: 'Poppins',
      fontSize: 10,
      padding: 10,
      width: '60mm',
    },
    header: {
      textAlign: 'center',
      marginBottom: 10,
    },
    data: {
      justifyContent: 'center',
      flexDirection: 'row',
    },
    title: {
      fontSize: 20,
      fontWeight: 600
    },
    logo: {
      width: 150,
      height: 50,
      margin: '0 auto',
      marginBottom: 10
    },
    section: {
      justifyContent: 'flex-end',
      flexDirection: 'row',
    },
    fwNormal: {
      fontWeight: 'normal',
    },
    fwSemiBold: {
      fontWeight: 700,
    },   
    fwBold: {
      fontWeight: 800,
    },  
    subtitle: {
      fontWeight: 700,
      marginRight: 3
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
    },
    tableColTitle: {
      width: '33%',
      fontWeight: 600,
      backgroundColor: '#e9e9e9'
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


  return (    
    data ? (
        <PDFViewer style={{ width: '99.5%', height: '106%' }}>
          <Document>
            <Page size="Letter" style={styles.page}>
              <View style={styles.header}>
                <Image style={styles.logo} src={logo} />
                <View style={styles.data}>
                  <Text style={styles.subtitle}>Calle:</Text>
                  <Text>HOLASOYVANESSA #12</Text>
                </View>
                <View style={styles.data}>
                  <Text style={styles.subtitle}>RFC:</Text>
                  <Text>HOLAGRUPO12</Text>
                </View>
                <View style={styles.data}>
                  <Text style={styles.subtitle}>Tel:</Text>
                  <Text>3481468309</Text>
                </View>
                <View style={styles.data}>
                  <Text style={styles.subtitle}>Caja:</Text>
                  <Text>{`${data.users.username}`}</Text>
                </View>
                <View style={styles.data}>
                  <Text style={styles.subtitle}>Fecha:</Text>
                  <Text>{`${data.date_reg}`}</Text>
                </View>
                <View style={styles.data}>
                  <Text style={styles.subtitle}>Recibo:</Text>
                  <Text>{`#${data.id}`}</Text>
                </View>
              </View>
              
              <View style={styles.table}>
                <View style={styles.tableRow}>
                  <View style={styles.tableColTitle}>
                    <Text style={styles.tableCell}>#</Text>
                  </View>
                  <View style={styles.tableColTitle}>
                    <Text style={styles.tableCell}>Producto</Text>
                  </View>
                  <View style={styles.tableColTitle}>
                    <Text style={styles.tableCell}>Precio</Text>
                  </View>
                  <View style={styles.tableColTitle}>
                    <Text style={styles.tableCell}>Total</Text>
                  </View>
                </View>
                { data.detail_sales.map((item, index) => (
                  <View style={styles.tableRow}>
                    <View style={styles.tableCol}>
                      <Text style={styles.tableCell}>{item.quantity}</Text>
                    </View>
                    <View style={styles.tableCol}>
                      <Text style={styles.tableCell}>{item.products.name}</Text>
                    </View>
                    <View style={styles.tableCol}>
                      <Text style={styles.tableCell}>${item.price}</Text>
                    </View>
                    <View style={styles.tableCol}>
                      <Text style={styles.tableCell}>${item.quantity * item.price}</Text>
                    </View>
                  </View>
                ))}                
              </View>
              
              <View style={styles.section}>
                <Text style={styles.subtitle}>Total:</Text>
                <Text>${data.total}</Text>
              </View>
            </Page>
          </Document>
        </PDFViewer>
      ) : <div>Loading...</div>
  );
};

export default PDFTicket;