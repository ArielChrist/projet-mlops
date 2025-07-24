// src/components/PredictionForm.js

import React, { useState } from 'react';
import { predict } from '../services/PredictionService';

const PredictionForm = () => {
  const [inputs, setInputs] = useState({
    date: '',
    bedrooms: '',
    bathrooms: '',
    sqft_living: '',
    sqft_lot: '',
    floors: '',
    waterfront: '',
    view: '',
    condition: '',
    sqft_above: '',
    sqft_basement: '',
    yr_built: '',
    yr_renovated: '',
    street: '',
    city: '',
    statezip: '',
    country: '',
  });

  const [result, setResult] = useState(null);
  const [error, setError] = useState('');

  const handleChange = e => {
    const { name, value } = e.target;
    setInputs(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async e => {
    e.preventDefault();
    setError('');
    setResult(null);

    const payload = {
      date: inputs.date,
      bedrooms: parseFloat(inputs.bedrooms),
      bathrooms: parseFloat(inputs.bathrooms),
      sqft_living: parseFloat(inputs.sqft_living),
      sqft_lot: parseFloat(inputs.sqft_lot),
      floors: parseFloat(inputs.floors),
      waterfront: parseInt(inputs.waterfront, 10),
      view: parseInt(inputs.view, 10),
      condition: parseInt(inputs.condition, 10),
      sqft_above: parseFloat(inputs.sqft_above),
      sqft_basement: parseFloat(inputs.sqft_basement),
      yr_built: parseInt(inputs.yr_built, 10),
      yr_renovated: parseInt(inputs.yr_renovated, 10),
      street: inputs.street,
      city: inputs.city,
      statezip: inputs.statezip,
      country: inputs.country,
    };

    try {
      const { price } = await predict(payload);
      setResult(price);
    } catch (err) {
      setError(err.message);
    }
  };

  const fields = [
    { name: 'date', type: 'text', label: 'Date' },
    { name: 'street', type: 'text', label: 'Rue' },
    { name: 'city', type: 'text', label: 'Ville' },
    { name: 'statezip', type: 'text', label: 'État/ZIP' },
    { name: 'country', type: 'text', label: 'Pays' },
    { name: 'bedrooms', type: 'number', label: 'Nombre de chambres' },
    { name: 'bathrooms', type: 'number', label: 'Nombre de salles de bain' },
    { name: 'sqft_living', type: 'number', label: 'Surface habitable (sqft)' },
    { name: 'sqft_lot', type: 'number', label: 'Surface terrain (sqft)' },
    { name: 'floors', type: 'number', label: 'Nombre d\'étages' },
    { name: 'waterfront', type: 'number', label: 'Waterfront (0 ou 1)' },
    { name: 'view', type: 'number', label: 'Indice de vue (0–4)' },
    { name: 'condition', type: 'number', label: 'Condition (1–5)' },
    { name: 'sqft_above', type: 'number', label: 'Surface au-dessus du sol (sqft)' },
    { name: 'sqft_basement', type: 'number', label: 'Surface du sous-sol (sqft)' },
    { name: 'yr_built', type: 'number', label: 'Année de construction' },
    { name: 'yr_renovated', type: 'number', label: 'Année de rénovation' },
  ];

  return (
    <div className="container my-5">
      <div className="card shadow-sm">
        <div className="card-body">
          <h3 className="card-title mb-4 text-center">
            Prédiction du prix de la maison
          </h3>

          <form onSubmit={handleSubmit}>
            <div className="row">
              {fields.map(field => (
                <div className="col-md-6 mb-3" key={field.name}>
                  <label htmlFor={field.name} className="form-label">
                    {field.label}
                  </label>
                  <input
                    id={field.name}
                    name={field.name}
                    type={field.type}
                    step={field.type === 'number' ? 'any' : undefined}
                    className="form-control"
                    value={inputs[field.name]}
                    onChange={handleChange}
                    required
                  />
                </div>
              ))}
            </div>

            <div className="d-grid gap-2">
              <button type="submit" className="btn btn-primary btn-lg">
                Prédire
              </button>
            </div>
          </form>

          {result !== null && (
            <div className="alert alert-success mt-4" role="alert">
              <h5>Prix prédit :</h5>
              <p className="mb-0">
                <strong>${result.toLocaleString()}</strong>
              </p>
            </div>
          )}

          {error && (
            <div className="alert alert-danger mt-4" role="alert">
              Erreur : {error}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default PredictionForm;