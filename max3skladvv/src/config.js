// Этот файл берет переменную из .env или использует заглушку
export const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";
//export const API_URL = "http://192.168.160.137:8000"; 

// Можно добавить эндпоинты для удобства
export const ENDPOINTS = {
    GOODS: `${API_URL}/goods/`,
    STOCKS: `${API_URL}/stocks/`,
    GOODINCOMES: `${API_URL}/goodincomes/`,
    GOODMOVES: `${API_URL}/goodmoves/`, 
    GOODRESTS: `${API_URL}/goodrests/`,      
    AI_REPORT: `${API_URL}/ai-report/`,
};
