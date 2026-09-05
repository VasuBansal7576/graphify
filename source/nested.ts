import { Base, Result } from "./base.js";
export function factory() { class Hidden extends Base { method(): Result { return {value:"a"}; } } return Hidden; }
it("case", () => { class Visible extends Base { method(): Result { return {value:"a"}; } } });
