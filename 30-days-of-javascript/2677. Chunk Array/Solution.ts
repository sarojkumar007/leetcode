type JSONValue =
  | null
  | boolean
  | number
  | string
  | JSONValue[]
  | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function chunk(arr: Obj[], size: number): Obj[][] {
  const ans: Obj[][] = [];
  let index: number = 0;

  while (index < arr.length) {
    ans.push(arr.slice(index, index + size));
    index += size;
  }

  return ans;
}
