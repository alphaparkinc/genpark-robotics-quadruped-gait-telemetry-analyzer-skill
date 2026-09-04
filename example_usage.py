from client import RoboticsQuadrupedGaitTelemetryAnalyzerClient

def main():
    client = RoboticsQuadrupedGaitTelemetryAnalyzerClient()
    res = client.analyze_gait_telemetry()
    print('Quadruped Gait Analyzer: ' + res['telemetry_session_id'] + ' (' + res['robot_id'] + ')')
    print('Stability: ' + str(res['gait_stability_index']) + ' | Slippage: ' + str(res['surface_slippage_detected']))
    print('Stream URL: ' + res['telemetry_stream_url'])

if __name__ == '__main__':
    main()
