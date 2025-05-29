# 📧 MCP Server Collection - Email & Beyond

> A comprehensive guide and collection of Model Context Protocol (MCP) servers for VS Code, featuring email integration, setup guides, and practical examples.

## 🚀 What is MCP?

Model Context Protocol (MCP) allows you to extend AI assistants like Claude with additional capabilities through local servers. Think of it as plugins that run on your machine and give Claude superpowers!

## 📋 Table of Contents

- [🎯 Features](#-features)
- [⚡ Quick Start](#-quick-start)
- [📧 Email Integration](#-email-integration)
- [🛠️ Available Servers](#️-available-servers)
- [💻 System Requirements](#-system-requirements)
- [📖 Setup Guides](#-setup-guides)
- [🧪 Testing](#-testing)
- [🚨 Troubleshooting](#-troubleshooting)
- [🤝 Contributing](#-contributing)

## 🎯 Features

- **📤 Email Integration**: Send emails directly from VS Code using various providers
- **🔧 Multiple Providers**: Support for Gmail, Outlook, Titan Email, and custom SMTP
- **🏠 Local Processing**: All servers run locally for maximum privacy and security
- **⚡ VS Code Integration**: Seamless integration with Claude for VS Code extension
- **🔌 Extensible**: Easy to add new servers and capabilities
- **📚 Well Documented**: Complete setup guides with emojis for clarity

## ⚡ Quick Start

### 1. Install VS Code Extension
```bash
# Install Claude for VS Code extension from the marketplace
```

### 2. Clone This Repository
```bash
git clone https://github.com/yourusername/mcp-server-collection.git
cd mcp-server-collection
```

### 3. Install Dependencies
```bash
npm install
```

### 4. Configure Your First Server
```bash
cp .env.example .env
# Edit .env with your credentials
```

### 5. Start Using!
```json
{
  "mcpServers": {
    "email": {
      "command": "node",
      "args": ["servers/email-server.js"],
      "cwd": "/path/to/this/project"
    }
  }
}
```

## 📧 Email Integration

### Supported Providers
- **📬 Titan Email** - Professional email hosting
- **📮 Gmail** - Google's email service
- **📪 Outlook** - Microsoft's email service
- **🔧 Custom SMTP** - Any SMTP provider

### Example Usage
```
"Send an email to client@example.com with subject 'Project Update 📊' and message 'The project is on track!'"
```

### Features
- ✅ Send plain text and HTML emails
- ✅ CC and BCC support
- ✅ Connection testing
- ✅ Error handling and logging
- ✅ Secure credential management

## 🛠️ Available Servers

| Server | Description | Status | Provider |
|--------|-------------|--------|----------|
| 📧 **Email Server** | Send emails via SMTP | ✅ Ready | Multiple |
| 📁 **Filesystem** | File operations | ✅ Ready | Local |
| 🔄 **Git Server** | Git repository management | ✅ Ready | Local |
| 🗄️ **Database** | Database connectivity | 🚧 In Progress | Multiple |
| 🌐 **Web Scraper** | Web content extraction | 📋 Planned | Various |
| ☁️ **AWS Integration** | AWS services access | 📋 Planned | Amazon |

## 💻 System Requirements

### Minimum Requirements
- **OS**: Windows 10+, macOS 10.15+, or Linux
- **Node.js**: Version 16.0+
- **RAM**: 4GB (8GB recommended)
- **Storage**: 100MB for base installation

### Recommended Setup
- **RAM**: 8GB+ for multiple servers
- **CPU**: Multi-core processor
- **Network**: Stable internet connection
- **VS Code**: Latest version

## 📖 Setup Guides

### 📧 Titan Email Setup
Complete guide for setting up Titan Email integration:

1. **Environment Configuration**
```env
TITAN_EMAIL=your-email@yourdomain.com
TITAN_PASSWORD=your-password
SMTP_HOST=smtp.titan.email
SMTP_PORT=587
```

2. **Server Configuration**
```javascript
const transporter = nodemailer.createTransporter({
  host: process.env.SMTP_HOST,
  port: parseInt(process.env.SMTP_PORT),
  secure: false,
  auth: {
    user: process.env.TITAN_EMAIL,
    pass: process.env.TITAN_PASSWORD
  }
});
```

3. **VS Code Integration**
```json
{
  "mcpServers": {
    "titan-email": {
      "command": "node",
      "args": ["servers/titan-email-server.js"],
      "cwd": "/path/to/project"
    }
  }
}
```

### 🔧 Adding New Servers
1. Create server file in `/servers/` directory
2. Implement MCP protocol handlers
3. Add configuration to examples
4. Update documentation
5. Test thoroughly

## 🧪 Testing

### Run Tests
```bash
npm test
```

### Test Individual Servers
```bash
# Test email server
npm run test:email

# Test connection
npm run test:connection
```

### Manual Testing
Use these commands in VS Code with Claude:
```
"Test the email connection"
"Send a test email to test@example.com"
"List available MCP tools"
```

## 🚨 Troubleshooting

### Common Issues

#### ❌ Server Won't Start
- ✅ Check Node.js version (`node --version`)
- ✅ Verify dependencies installed (`npm install`)
- ✅ Check file paths in configuration
- ✅ Review error logs

#### ❌ Email Connection Failed
- ✅ Verify SMTP credentials
- ✅ Check firewall/antivirus settings
- ✅ Try different SMTP ports (587, 465, 25)
- ✅ Enable "less secure apps" if required

#### ❌ VS Code Integration Issues
- ✅ Restart VS Code
- ✅ Check MCP configuration file location
- ✅ Verify Claude extension is installed
- ✅ Review VS Code console for errors

### Debug Mode
Enable debug logging:
```env
DEBUG=mcp:*
NODE_ENV=development
```

## 📊 Performance & Limits

### Resource Usage
- **Per Server**: ~10-50MB RAM
- **Recommended Limit**: 15-20 servers for optimal performance
- **Network**: Minimal usage except during active operations

### Scaling Considerations
- Start with 3-5 essential servers
- Add servers based on actual needs
- Monitor system performance
- Consider server grouping for large setups

## 🔒 Security Best Practices

- 🔐 Store credentials in environment variables
- 🚫 Never commit sensitive data to git
- 🔄 Rotate passwords regularly
- 🛡️ Use app-specific passwords when available
- 🏠 Keep servers local-only
- 📝 Review server permissions regularly

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### 🐛 Bug Reports
- Use GitHub issues
- Include system information
- Provide reproduction steps
- Add relevant logs

### ✨ Feature Requests
- Check existing issues first
- Describe the use case
- Explain expected behavior
- Consider implementation impact

### 🔧 Pull Requests
1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

### 📋 Development Setup
```bash
git clone https://github.com/yourusername/mcp-server-collection.git
cd mcp-server-collection
npm install
npm run dev
```

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Anthropic](https://anthropic.com) for the MCP protocol
- [Node.js](https://nodejs.org) community
- [Nodemailer](https://nodemailer.com) for email functionality
- Contributors and testers

## 📞 Support

- 📧 Email: [contact@rifaterdemsahin.com]
- 💬 Discussions: [GitHub Discussions](https://github.com/rifaterdemsahin)
- 🐛 Issues: [GitHub Issues](https://github.com/rifaterdemsahin/mcpservers_forworkstations/issues)
- 📖 Wiki: [Project Wiki](https://github.com/rifaterdemsahin/mcpservers_forworkstations/wiki)

---

**⭐ If this project helps you, please give it a star!** 

**🔄 Stay updated**: Watch this repository for the latest features and improvements.

**🤖 Built with ❤️ for the MCP community**