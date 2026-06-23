/**
 * Real-time Dashboard Updates for Inventory Dashboard
 * Polls the API endpoint and updates dashboard statistics in real-time
 */

class RealtimeInventoryDashboard {
    constructor() {
        this.apiUrl = '/inventory/api/dashboard/';
        this.pollInterval = 5000; // 5 seconds
        this.pollTimer = null;
        this.isPolling = false;
        
        this.init();
    }
    
    init() {
        // Wait for DOM to be ready
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => this.start());
        } else {
            this.start();
        }
    }
    
    start() {
        // Check if we're on the inventory dashboard page
        const dashboardElement = document.getElementById('inventory-dashboard');
        if (!dashboardElement) {
            console.log('Inventory dashboard element not found, skipping real-time updates');
            return; // Not on the dashboard page
        }
        
        console.log('Inventory dashboard element found, starting real-time updates');
        
        // Initial fetch
        this.fetchDashboardData();
        
        // Start polling
        this.pollTimer = setInterval(() => this.fetchDashboardData(), this.pollInterval);
        
        // Re-fetch when window regains focus (e.g., tab switch)
        document.addEventListener('visibilitychange', () => {
            if (document.visibilityState === 'visible') {
                console.log('Page became visible, fetching fresh inventory data');
                this.fetchDashboardData(); // Immediately check when page becomes visible
            }
        });
    }
    
    async fetchDashboardData() {
        if (this.isPolling) {
            return; // Prevent concurrent requests
        }
        
        try {
            this.isPolling = true;
            
            console.log('Fetching inventory dashboard data from:', this.apiUrl);
            
            // Get CSRF token from cookie
            const csrfToken = this.getCookie('csrftoken');
            const headers = {
                'X-Requested-With': 'XMLHttpRequest',
            };
            if (csrfToken) {
                headers['X-CSRFToken'] = csrfToken;
            }
            
            const response = await fetch(this.apiUrl, {
                method: 'GET',
                headers: headers,
                credentials: 'same-origin'
            });
            
            console.log('API Response Status:', response.status);
            
            if (!response.ok) {
                const errorText = await response.text();
                console.error('API Error Response:', errorText);
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            const data = await response.json();
            console.log('Inventory dashboard data received:', data);
            
            // Update dashboard with new data
            this.updateDashboard(data);
            
        } catch (error) {
            console.error('Error fetching inventory dashboard data:', error);
            // Silently fail - don't disturb user experience
        } finally {
            this.isPolling = false;
        }
    }
    
    updateDashboard(data) {
        if (!data || !data.statistics) {
            return;
        }
        
        // Update statistics cards
        this.updateStatisticsCards(data.statistics);
    }
    
    updateStatisticsCards(statistics) {
        // Update Total Medicines
        const totalMedicinesElement = document.getElementById('stat-total-medicines');
        if (totalMedicinesElement) {
            totalMedicinesElement.textContent = statistics.total_medicines || 0;
        }
        
        // Update Low Stock Medicines
        const lowStockElement = document.getElementById('stat-low-stock');
        if (lowStockElement) {
            lowStockElement.textContent = statistics.low_stock_medicines || 0;
        }
        
        // Update Pending Orders
        const pendingOrdersElement = document.getElementById('stat-pending-orders');
        if (pendingOrdersElement) {
            pendingOrdersElement.textContent = statistics.pending_orders || 0;
        }
        
        // Update Total Manufacturers
        const totalManufacturersElement = document.getElementById('stat-total-manufacturers');
        if (totalManufacturersElement) {
            totalManufacturersElement.textContent = statistics.total_manufacturers || 0;
        }
    }
    
    getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    stop() {
        if (this.pollTimer) {
            clearInterval(this.pollTimer);
            this.pollTimer = null;
        }
    }
}

// Initialize real-time inventory dashboard when script loads
console.log('Real-time inventory dashboard script loaded');
new RealtimeInventoryDashboard();
