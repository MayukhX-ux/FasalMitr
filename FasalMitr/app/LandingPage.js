import React, { useState } from 'react';
import { View, Text, TextInput, Button, TouchableOpacity, StyleSheet } from 'react-native';

export default function LandingPage({ navigation }) {
  const [name, setName] = useState('');
  const [age, setAge] = useState('');
  const [farmerType, setFarmerType] = useState('');
  const [yearSince, setYearSince] = useState('');
  const [useType, setUseType] = useState('');

  (function handleRegister() { 
    // Pass registration data to Dashboard screen via navigation params
    navigation.navigate('Dashboard', {
      name,
      age,
      farmerType,
      yearSince,
      useType,
    });
    }
  );

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Welcome to FasalMitr</Text>
      <Text style={styles.subHeader}>Register your profile</Text>
      <TextInput
        style={styles.input}
        placeholder="Name"
        value={name}
        onChangeText={setName}
      />
      <TextInput
        style={styles.input}
        placeholder="Age"
        value={age}
        onChangeText={setAge}
        keyboardType="numeric"
      />

      <Text style={styles.label}>Are you...</Text>
      <View style={styles.buttonRow}>
        <TouchableOpacity
          style={[
            styles.optionButton,
            farmerType === 'existing' && styles.selectedButton,
          ]}
          onPress={() => setFarmerType('existing')}
        >
          <Text>Already Existing Farmer</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[
            styles.optionButton,
            farmerType === 'beginner' && styles.selectedButton,
          ]}
          onPress={() => setFarmerType('beginner')}
        >
          <Text>Beginner</Text>
        </TouchableOpacity>
      </View>

      {farmerType === 'existing' && (
        <TextInput
          style={styles.input}
          placeholder="Year Since Farming (e.g., 2010)"
          value={yearSince}
          onChangeText={setYearSince}
          keyboardType="numeric"
        />
      )}

      {farmerType === 'beginner' && (
        <View>
          <Text style={styles.label}>Use:</Text>
          <View style={styles.buttonRow}>
            <TouchableOpacity
              style={[
                styles.optionButton,
                useType === 'personal' && styles.selectedButton,
              ]}
              onPress={() => setUseType('personal')}
            >
              <Text>Personal</Text>
            </TouchableOpacity>
            <TouchableOpacity
              style={[
                styles.optionButton,
                useType === 'commercial' && styles.selectedButton,
              ]}
              onPress={() => setUseType('commercial')}
            >
              <Text>Commercial</Text>
            </TouchableOpacity>
          </View>
        </View>
      )}

      <Button title="Register" onPress={handleRegister} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', padding: 20 },
  header: { fontSize: 24, fontWeight: 'bold', marginBottom: 10 },
  subHeader: { fontSize: 18, marginBottom: 20 },
  input: { borderWidth: 1, borderColor: '#ccc', padding: 8, marginVertical: 8, borderRadius: 5 },
  label: { fontSize: 16, marginTop: 10 },
    optionButton: {
      flex: 1,
      padding: 10,
      marginHorizontal: 5,
    },
  })