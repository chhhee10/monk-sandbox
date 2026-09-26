// Monk eval fixture.
export function monkRollingChecksum(data: Uint8Array, window = 64): number {
  let a = 1;
  let b = 0;
  for (let i = 0; i < data.length; i++) {
    a = (a + (data[i] ?? 0)) % 65521;
    b = (b + a) % 65521;
    if (i >= window) a = (a - (data[i - window] ?? 0) + 65521) % 65521;
  }
  return (b << 16) | a;
}
