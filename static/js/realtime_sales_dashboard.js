/**
 * Real-time updates for Sales Representative dashboard (/orders/)
 * Updates statistics cards and recent orders status table.
 */

class RealtimeSalesDashboard {
    constructor() {
        this.apiUrl = '/orders/api/sales-rep/dashboard/';
        this.pollInterval = 5000; // 5 seconds
        this.pollTimer = null;
        this.isPolling = false;

        this.init();
    }

    init() {
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => this.start());
        } else {
            this.start();
        }
    }

    start() {
        const dashboardElement = document.getElementById('sales-rep-dashboard');
        if (!dashboardElement) {
            return;
        }

        this.fetchDashboardData();
        this.pollTimer = setInterval(() => this.fetchDashboardData(), this.pollInterval);

        document.addEventListener('visibilitychange', () => {
            if (document.visibilityState === 'visible') {
                this.fetchDashboardData();
            }
        });
    }

    async fetchDashboardData() {
        if (this.isPolling) {
            return;
        }

        try {
            this.isPolling = true;

            const response = await fetch(this.apiUrl, {
                method: 'GET',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                },
                credentials: 'same-origin',
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            this.updateDashboard(data);
        } catch (error) {
            console.error('Error fetching sales dashboard data:', error);
        } finally {
            this.isPolling = false;
        }
    }

    updateDashboard(data) {
        if (!data || !data.statistics) {
            return;
        }

        this.updateStatisticsCards(data.statistics);

        if (data.recent_orders) {
            this.updateRecentOrders(data.recent_orders);
        }
    }

    updateStatisticsCards(statistics) {
        this.updateText('stat-total-orders', statistics.total_orders);
        this.updateText('stat-pending-orders', statistics.pending_orders);
        this.updateText('stat-processing-orders', statistics.processing_orders);
        this.updateText('stat-confirmed-orders', statistics.confirmed_orders);
        this.updateText('stat-ready-orders', statistics.ready_orders);
    }

    updateText(elementId, value) {
        const element = document.getElementById(elementId);
        if (element) {
            element.textContent = value || 0;
        }
    }

    updateRecentOrders(recentOrders) {
        const tbody = document.getElementById('recent-orders-tbody');
        if (!tbody) {
            return;
        }

        tbody.innerHTML = '';

        if (recentOrders.length === 0) {
            tbody.innerHTML = `
                <tr>
                    <td colspan="5" class="text-center py-4">
                        <i class="fas fa-inbox fa-2x text-muted mb-2"></i>
                        <p class="text-muted mb-0">No recent orders found</p>
                    </td>
                </tr>
            `;
            return;
        }

        recentOrders.forEach((order) => {
            const row = document.createElement('tr');
            const statusBadgeClass = this.getStatusBadgeClass(order.status);

            row.innerHTML = `
                <td>#${order.id}</td>
                <td>${this.escapeHtml(order.created_at_display)}</td>
                <td>
                    <span class="badge bg-${statusBadgeClass}">
                        ${this.escapeHtml(order.status_display)}
                    </span>
                </td>
                <td>₱${parseFloat(order.total_amount).toFixed(2)}</td>
                <td>
                    <a href="/orders/orders/${order.id}/" class="btn btn-sm btn-outline-primary">
                        <i class="fas fa-eye"></i> View
                    </a>
                </td>
            `;

            tbody.appendChild(row);
        });
    }

    getStatusBadgeClass(status) {
        const statusMap = {
            pending: 'warning',
            confirmed: 'info',
            processing: 'info',
            ready_for_pickup: 'success',
            shipped: 'info',
            delivered: 'dark',
            cancelled: 'danger',
            returned: 'warning',
        };

        return statusMap[status] || 'secondary';
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
}

new RealtimeSalesDashboard();
