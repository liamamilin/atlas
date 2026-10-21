export const auxiliaryWorkflowSteps = [
  ["existing_template", "检查已有模板", "Check existing templates"],
  ["scenario", "确定场景", "Define scenario"],
  ["case_research", "案例研究", "Case research"],
  ["generation", "生成模板", "Generate template"],
  ["deterministic_check", "确定性检查", "Deterministic checks"],
  ["independent_review", "独立审阅", "Independent review"],
  ["freeze_import", "冻结入库", "Freeze and import"],
  ["download", "验证下载", "Verify download"],
] as const;
export type WorkflowStepName = typeof auxiliaryWorkflowSteps[number][0];
export type WorkflowState = "pending" | "running" | "completed" | "reused" | "failed" | "paused";
export interface AuxiliaryStep { step: WorkflowStepName; state: WorkflowState; attempt: string; started?: number | null; finished?: number | null; input_digest?: string; outputs: {path: string;sha256: string;url?: string}[]; error?: string; code?: string }
export interface AuxiliaryItem { leaf: string; display_name: string; state: string; artifact_id?: string; current_attempt?: string; failure_stage?: string; failure_code?: string; error?: string; steps: AuxiliaryStep[]; calls: {id:string;stage:string;status:string;requested_model:string;outcome?:string;started?:number|null;finished?:number|null}[] }
export interface AuxiliaryPlan { id:string;status:string;reason?:string;model:string;baseline:number;max_calls:number;new_calls:number;active_calls:number;remaining_calls:number;total:number;handled:number;counts:Record<string,number>;started?:number|null;deadline?:number|null;gate:{mode:"validation"|"full";leaves:string[];status:string}|null }
export interface AuxiliaryPlanDetail {plan:AuxiliaryPlan;items:AuxiliaryItem[];pagination:{offset:number;limit:number;total:number}}
