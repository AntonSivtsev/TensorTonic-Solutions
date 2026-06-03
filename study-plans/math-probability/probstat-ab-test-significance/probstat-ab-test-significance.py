from scipy import stats

def ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, alpha):
    """
    Returns: [p_control, p_treatment, z_stat, p_value, reject] as a list.
    """
    p_control = control_conversions / control_visitors
    p_treatment = treatment_conversions / treatment_visitors
    p = (control_conversions + treatment_conversions) / (control_visitors + treatment_visitors)
    se = (p*(1 - p)*(1/control_visitors + 1/treatment_visitors)) ** 0.5
    z = round((p_treatment - p_control) / se, 4)
    p_value = round(2 * stats.norm.sf(abs(z)), 4)
    if p_value < alpha:
        r = True
    else:
        r = False
        
    return [p_control, p_treatment, z, p_value, r]