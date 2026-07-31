const { execSync } = require('child_process');
const path = require('path');

const backendDir = path.join(__dirname, '..', '..', 'backend');
const pythonBin = process.platform === 'win32'
  ? path.join(backendDir, 'venv', 'Scripts', 'python')
  : path.join(backendDir, 'venv', 'bin', 'python');

execSync(`"${pythonBin}" -m PyInstaller --noconfirm build.spec`, {
  stdio: 'inherit',
  cwd: backendDir
});
