enum OS {
  LINUX,
  MAC,
  WINDOWS,
}

const osInfo: {
  version: number;
  os: OS;
} = {
  version: 1,
  os: OS.WINDOWS,
};

console.log(osInfo);
