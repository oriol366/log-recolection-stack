# Monitoring Stack with Grafana, Loki, Promtail, and Telegram Alerts

This project sets up a monitoring stack using Grafana, Loki, and Promtail. It includes a Python application that logs messages. The stack is configured to send alerts to a Telegram bot when error logs are detected.

## Project Structure

```
log-recolection-stack/
│
├── docker-compose.yml
├── grafana/
│   ├── provisioning/
│   │   ├── datasources/
│   │   │   └── datasource.yml
│   │   ├── dashboards/
│   │   │   └── dashboard.yml
│   │   ├── alerting/
│   │   │   └── notifier.yml
│   └── dashboards/
│       └── default.json
├── loki/
│   └── config.yml
├── promtail/
│   └── config.yml
└── src/
    ├── Dockerfile
    ├── main.py
    ├── requirements.txt
```

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/oriol366/log-recolection-stack.git
   cd log-recolection-stack
   ```

2. **Set up environment variables:**

   Create a `.env` file in the root of the project directory with the following content:

   ```env
    GF_ALERTING_NOTIFICATION_TELEGRAM_BOT_TOKEN=your_bot_token_here
    GF_ALERTING_NOTIFICATION_TELEGRAM_CHAT_ID=your_chat_id_here
   ```

4. **Build and start the Docker containers:**

   ```sh
   docker-compose up --build -d
   ```

### Configuration Details

#### Grafana

- **Datasource:** Configured to use Loki as the data source.
- **Dashboards:** Sample dashboard to visualize logs.
- **Alerting:** Alerts configured to detect error logs and notify via Telegram.
- **Notifiers:** Configured to use a Telegram bot for notifications.

#### Loki

- **Config File:** `loki/config.yml`

#### Promtail

- **Config File:** `promtail/config.yml`


### Viewing Logs

Logs from the Python application and other services are collected and displayed in Grafana dashboards. You can access Grafana at `http://localhost:3000` with default credentials (`admin`/`admin`).

## Troubleshooting


### Logs

Check the logs of the services using Docker Compose:

```sh
docker-compose logs loki
docker-compose logs promtail
docker-compose logs grafana
```

## Contributing

Feel free to open issues or submit pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.